from django import forms

from .models import Photo


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("file", )

