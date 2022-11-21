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
    recipient_full_name = models.CharField(
        max_length=300,
        verbose_name='ФИО получателя',
        help_text='Укажите ФИО получателя письма, полностью. Например: Иванов Иван Иванович.'
    )
    postal_address = models.TextField(
        verbose_name='Адрес проживания',
        help_text='Укажите название улицы, дома, квартиры. Например ул.Красного знамени, д.19, кв.2'
    )
    locality = models.CharField(
        max_length=30,
        verbose_name='Населённый пункт',
        help_text='Укажите ваш населённый пункт.'
    )
    country_subject = models.CharField(
        max_length=30,
        verbose_name='Территориальный субъект',
        help_text='Укажите ваш район, область, край или республику. Например: Приморский край.'
    )
    zip_code = models.CharField(
        max_length=6,
        verbose_name='Почтовый индекс',
        help_text='Укажите индекс вашего почтового отделения.'
    )
    social_network_nickname = models.CharField(
        max_length=60, verbose_name='Имя в социальной сети',
        help_text='Не забудьте указать название социальной сети'
    )

    date_action_use = models.DateTimeField(
        default=timezone.now(),
        verbose_name='дата использования функции "найти друзей"'
    )
    user_friends = models.TextField(
        blank=True,
        null=True,
        verbose_name='список друзей пользователя'
    )
