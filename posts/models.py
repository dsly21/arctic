from django.conf import settings
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    title = models.CharField(
        max_length=256,
        verbose_name='заголовок'
    )
    main_image = models.ImageField(
        'Главное изображение',
        upload_to='posts/',
        blank=True,
        null=True,
        help_text='Это изображение будет расположено на самом верху поста.'
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

    def get_post_images(self):
        return self.image_set.select_related('post')

    def get_post_video(self):
        return self.video_set.select_related('post').first()


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


class Video(models.Model):
    video = EmbedVideoField(
        blank=True,
        null=True,
        verbose_name='видео'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )


class ContactInformation(models.Model):
    email = models.EmailField(verbose_name='электронная почта')
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='телефонный номер'
    )

    class Meta:
        verbose_name = 'Контакты'


class UserfulLinks(models.Model):
    link = models.TextField(verbose_name='ссылка')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'


