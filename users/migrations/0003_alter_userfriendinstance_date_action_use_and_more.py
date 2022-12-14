# Generated by Django 4.1.2 on 2022-11-23 11:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userfriendinstance_country_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfriendinstance',
            name='date_action_use',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 11, 0, 19, 381729, tzinfo=datetime.timezone.utc), verbose_name='дата использования функции "найти друзей"'),
        ),
        migrations.AlterField(
            model_name='userfriendinstance',
            name='social_network_nickname',
            field=models.CharField(help_text='Например id222829594', max_length=60, verbose_name='Укажите как вас найти "вконтакте"'),
        ),
        migrations.AlterField(
            model_name='userfriendinstance',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfriendinstance',
            name='user_friends',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL, verbose_name='список друзей пользователя'),
        ),
    ]
