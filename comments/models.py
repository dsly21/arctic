from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.utils import timezone

from posts.models import Post


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='автор',
    )
    text = RichTextField(
        verbose_name='текст'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='пост'
    )
    comment_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата публикации'
    )
