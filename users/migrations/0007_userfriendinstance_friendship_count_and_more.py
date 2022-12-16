# Generated by Django 4.1.2 on 2022-12-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_userfriendinstance_country_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfriendinstance',
            name='friendship_count',
            field=models.IntegerField(default=0, verbose_name='количество друзей'),
        ),
        migrations.AlterField(
            model_name='userfriendinstance',
            name='user_friends',
            field=models.JSONField(blank=True, default=list, verbose_name='список друзей пользователя'),
        ),
    ]
