from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='заголовок'
    )
    main_image = models.ImageField(
        'Главное изображение',
        upload_to='posts/',
        help_text='Это изображение будет расположено на миниатюре списка публикаций и в самом верху поста. '
                  'Внимание: название изображения должно быть на латинице. Пример: image.jpg'
    )
    main_video = EmbedVideoField(
        blank=True,
        null=True,
        verbose_name='главное видео',
        help_text='Видео будет расположено на верху страницы поста. Добавлять сюда видео нужно, когда видео ролик - это'
                  ' основной, заглавный контент поста.'
    )
    text = RichTextField(verbose_name='текст')
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

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

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
        help_text='Добавьте несколько изображений. Внимание: название изображения должно быть на латинице. '
                  'Пример: image.jpg'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


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

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class ContactInformation(models.Model):
    email = models.EmailField(
        verbose_name='электронная почта',
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='телефонный номер'
    )

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class UserfulLinks(models.Model):
    link = models.TextField(verbose_name='ссылка')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'


class AboutUs(models.Model):
    text = models.TextField(verbose_name='текст')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
