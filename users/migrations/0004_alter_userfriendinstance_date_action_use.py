# Generated by Django 4.1.2 on 2022-11-29 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userfriendinstance_date_action_use_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfriendinstance',
            name='date_action_use',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата использования функции "найти друзей"'),
        ),
    ]
