from django.conf import settings
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

SUBSCRIBERS = 'FROM_SUBSCRIBERS'
COMPETITION = 'COMPETITION'
BASE_POST = 'BASE_POST'
LINK_POST = 'LINK_POST'


class Post(models.Model):
    class PostType(models.TextChoices):
        SUBSCRIBERS = 'материал от подписчиков'
        COMPETITION = 'конкурс'
        BASE_POST = 'общий пост'
        LINK_POST = 'пост с ссылкой'

    title = models.CharField(
        max_length=256,
        verbose_name='заголовок'
    )
    text = models.TextField(verbose_name='текст')
    pub_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата публикации'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор'
    )
    images = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        null=True,
    )
    video = EmbedVideoField(
        blank=True,
        null=True,
        verbose_name='видео'
    )
    post_type = models.TextField(
        choices=PostType.choices,
        default=PostType.BASE_POST,
        verbose_name='тип публикации'
    )
    permission_publish = models.BooleanField(
        verbose_name='одобрено к публикации',
        default=False
    )


class Image(models.Model):
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        null=True,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )


class ContactInformation(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)


