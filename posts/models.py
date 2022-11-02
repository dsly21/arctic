from django.contrib.auth import get_user_model
from django.db import models

SUBSCRIBERS = 'FROM_SUBSCRIBERS'
COMPETITION = 'COMPETITION'
BASE_POST = 'BASE_POST'


User = get_user_model()


class Post(models.Model):
    class PostType(models.TextChoices):
        SUBSCRIBERS = 'материал от подписчиков'
        COMPETITION = 'конкурс'
        BASE_POST = 'общий пост'

    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField()
    post_type = models.TextField(
        choices=PostType.choices,
        default='общий пост',
    )


class UsefulLink(models.Model):
    link = models.URLField()
    description = models.TextField()

