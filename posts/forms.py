from django import forms

from posts.models import Post, Image


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'video',
            'post_type',
            #'permission_publish',
        ]
        # TODO: add permission_publish


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='изображение',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = Image
        fields = ['image', ]
