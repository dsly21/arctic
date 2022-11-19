from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    class UserRegion(models.TextChoices):
        ARCTIC = True
        NOT_ARCTIC = False

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    birth_year = models.IntegerField(
        verbose_name='дата рождения',
    )
    arctic_region_flag = models.TextField(
        choices=UserRegion.choices,
        verbose_name='арктический регион',
        default=UserRegion.NOT_ARCTIC,
    )


class UserFriendInstance(models.Model):
    class Meta:
        verbose_name = 'Пользователь в базе данных друзей'
        verbose_name_plural = 'Пользователи в базе данных друзей'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_network_nickname = models.CharField(
        max_length=60, verbose_name='Имя в социальной сети',
        help_text='Не забудьте указать название социальной сети'
    )
    postal_address = models.TextField(verbose_name='Адрес проживания')
    date_action_use = models.DateTimeField(
        default=timezone.now(),
        verbose_name='дата использования функции "найти друзей"'
    )
    user_friends = models.TextField(
        blank=True,
        null=True,
        verbose_name='список друзей пользователя'
    )
