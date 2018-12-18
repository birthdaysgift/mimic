from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View


from auth_custom.models import User
from friends.models import Friendship, FriendshipRequest
from photos.models import UserPhoto
from posts.models import Post
from posts.forms import AddPostForm
from videos.models import UserVideo

from .forms import EditPageForm


class PageView(LoginRequiredMixin, View):
    login_url = reverse_lazy("auth_custom:login")
    template_name = "pages/base.html"

    def get(self, request, username=None):
        # get page owner
        page_owner = get_object_or_404(User, username=username)

        # get posts and likes/dislikes for them
        posts = Post.objects.filter(receiver=page_owner)
        posts = posts.select_related('sender')
        posts = posts.order_by("-date", "-time")
        paginator = Paginator(posts, per_page=10)
        posts_page = paginator.page(1)
        posts = posts_page.object_list
        posts.attach_likes(check_user=request.user)
        if posts_page.has_next():
            next_posts_page = posts_page.next_page_number()
        else:
            next_posts_page = None

        # get user_photos
        user_photos = UserPhoto.objects.filter(user=page_owner)
        user_photos = user_photos.select_related("user", "photo")[:6]

        # get user_videos
        user_videos = UserVideo.objects.filter(user=page_owner)
        user_videos = user_videos.select_related("user", "video")[:6]

        # get friends
        friends = Friendship.objects.get_friends_of(page_owner,
                                                    strict_to=6,
                                                    random_order=True)

        # get friendship status
        is_friend = Friendship.objects.is_friends(request.user, page_owner)
        setattr(page_owner, 'is_friend', is_friend)
        friend_request_sent_by = FriendshipRequest.objects.who_sent_request(
            page_owner, request.user
        )

        context = {
            "form": AddPostForm(),
            "page_owner": page_owner,
            "posts": posts,
            "next_posts_page": next_posts_page,
            "friends": friends,
            'friend_request_sent_by': friend_request_sent_by,
            "user_photos": user_photos,
            "user_videos": user_videos,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, username=None):
        form = AddPostForm(request.POST)
        if form.is_valid():
            receiver = get_object_or_404(User, username=username)
            Post(
                sender=request.user,
                receiver=receiver,
                text=form.cleaned_data["text"]
            ).save()
            url = reverse('pages:page', kwargs={'username': username})
            return redirect(url)
        else:
            return render(request, self.template_name, context={"form": form})


class EditView(LoginRequiredMixin, View):
    template_name = "pages/edit.html"

    def get(self, request, username=None):
        page_owner = get_object_or_404(User, username=username)
        if request.user == page_owner:
            form = EditPageForm(instance=request.user)
            return render(request, self.template_name, context={"form": form})
        url = reverse('pages:page', kwargs={'username': username})
        return redirect(url)

    def post(self, request, username=None):
        form = EditPageForm(request.POST, request.FILES, instance=request.user)
        page_owner = get_object_or_404(User, username=username)
        if request.user == page_owner:
            if form.is_valid():
                form.save()
                kwargs = {"username": request.user.username}
                url = reverse('pages:page', kwargs=kwargs)
                return redirect(url)
            return render(request, self.template_name, context={"form": form})
        url = reverse('pages:page', kwargs={'username': username})
        return redirect(url)
