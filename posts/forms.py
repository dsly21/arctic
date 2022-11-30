from django import forms
from embed_video.fields import EmbedVideoFormField

from posts.models import Post, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'post_type',
            #'permission_publish',
        ]
        # TODO: add permission_publish


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', ]

    image = forms.ImageField(
        required=False,
        label='изображение',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )


class VideoForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['video', ]

    video = EmbedVideoFormField(
        label='видео',
        required=False,
        #widget=forms.ClearableFileInput(attrs={'multiple': True})
    )
