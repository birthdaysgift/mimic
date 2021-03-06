from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import RedirectView

from auth_custom.models import User

from .forms import TalksForm
from .models import PublicMessage, PrivateMessage, DialogDoesNotExist
from .utils import aligned_range_of_pages


class TalksView(LoginRequiredMixin, views.View):
    login_url = reverse_lazy("auth_custom:login")
    template = "talks/base.html"

    def get(self, request, receiver_name="global", page_num=1):
        # get messages
        if receiver_name == "global":
            dialog_messages = PublicMessage.objects.all()
        else:
            try:
                dialog_messages = PrivateMessage.objects.from_dialog(
                    request.user.username,
                    receiver_name
                )
            except DialogDoesNotExist:
                raise Http404
        dialog_messages = dialog_messages.order_by("-date", "-time")
        paginator = Paginator(dialog_messages, 10)
        dialog_messages = paginator.page(page_num).object_list
        dialog_messages = list(dialog_messages)
        dialog_messages.reverse()

        # get pages
        pages = aligned_range_of_pages(
            page=page_num,
            last_page=paginator.num_pages
        )
        if len(pages) == 1:
            pages = None

        friends = request.user.get_friends()

        # get contacts
        sent_messages = PrivateMessage.objects.filter(
            sender=request.user).distinct('receiver').select_related('receiver')
        received_messages = PrivateMessage.objects.filter(
            receiver=request.user).distinct('sender').select_related('sender')
        receivers = tuple(msg.receiver for msg in sent_messages)
        senders = tuple(msg.sender for msg in received_messages)
        contacts = list(set(receivers + senders))
        contacts.sort(key=lambda contact: contact.username)

        for contact in contacts:
            last_message = PrivateMessage.objects.filter(
                Q(sender=contact, receiver=request.user) |
                Q(sender=request.user, receiver=contact)
            ).last()
            setattr(contact, 'last_message', last_message)

        context = {
            "form": TalksForm(),
            "contacts": contacts,
            "friends": friends,
            "dialog_messages": dialog_messages,
            "pages": pages,
            "current_page": page_num,
            "receiver_name": receiver_name
        }
        return render(request, self.template, context=context)

    def post(self, request, receiver_name="global", page_num=1):
        form = TalksForm(request.POST)
        if form.is_valid():
            if receiver_name == "global":
                PublicMessage(
                    sender=request.user,
                    text=form.cleaned_data["message"]
                ).save()
            else:
                receiver = get_object_or_404(User, username=receiver_name)
                PrivateMessage(
                    sender=request.user,
                    receiver=receiver,
                    text=form.cleaned_data["message"]
                ).save()
            kwargs = {
                "receiver_name": receiver_name,
                "page_num": 1
            }
            url = reverse("talks:talk", kwargs=kwargs)
            return redirect(url)
        else:
            return render(request, self.template, context={"form": form})


class RedirectToTalksView(RedirectView):
    url = reverse_lazy(
        'talks:talk', kwargs={'receiver_name': 'global', 'page_num': 1}
    )
