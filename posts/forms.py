from django import forms
from embed_video.fields import EmbedVideoFormField

from posts.models import Post, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'main_image',
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
        label='Изображение',
        help_text='Добавьте одно или несколько изображений.',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )


class VideoForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['video', ]

    video = EmbedVideoFormField(
        label='Видео',
        required=False,
        help_text='Добавьте сюда ссылку на видео, например: https://www.youtube.com/',
        #widget=forms.ClearableFileInput(attrs={'multiple': True})
    )
