from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    birth_year = models.IntegerField(
        verbose_name='дата рождения',
    )
    arctic_region_flag = models.BooleanField(
        verbose_name='арктический регион',
        default=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserFriendInstance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recipient_full_name = models.CharField(
        max_length=300,
        verbose_name='ФИО получателя',
        help_text='Укажите ФИО получателя письма, полностью. Например: Иванов Иван Иванович.'
    )
    postal_address = models.TextField(
        verbose_name='Полный адрес проживания',
        help_text='Например Якутская область, город Якутск, ул.Красного знамени, д.19, кв.2'
    )
    zip_code = models.CharField(
        max_length=6,
        verbose_name='Почтовый индекс',
        help_text='Укажите индекс вашего почтового отделения.'
    )
    social_network_nickname = models.CharField(
        max_length=60, verbose_name='Укажите как вас найти "вконтакте"',
        help_text='Например id222829594',
        blank=True,
        null=True,
    )

    date_action_use = models.DateTimeField(
        default=timezone.now,
        verbose_name='дата использования функции "найти друзей"'
    )
    user_friends = models.JSONField(
        blank=True,
        verbose_name='список друзей пользователя',
        default=list
    )
    friendship_count = models.IntegerField(
        verbose_name='количество друзей',
        default=0
    )

    class Meta:
        verbose_name = 'Пользователь в базе данных друзей'
        verbose_name_plural = 'Пользователи в базе данных друзей'
