from django.contrib.auth import get_user_model
from django.db import models
from embed_video.fields import EmbedVideoField

SUBSCRIBERS = 'FROM_SUBSCRIBERS'
COMPETITION = 'COMPETITION'
BASE_POST = 'BASE_POST'
LINK_POST = 'LINK_POST'

User = get_user_model()


class Post(models.Model):
    class PostType(models.TextChoices):
        SUBSCRIBERS = 'материал от подписчиков'
        COMPETITION = 'конкурс'
        BASE_POST = 'общий пост'
        LINK_POST = 'пост с ссылкой'

    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        null=True,
    )
    video = EmbedVideoField(blank=True, null=True)
    post_type = models.TextField(
        choices=PostType.choices,
        default='общий пост',
    )


class ContactInformation(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)


