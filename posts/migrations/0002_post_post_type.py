# Generated by Django 4.1.2 on 2022-11-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.TextField(blank=True, choices=[('FROM_SUBSCRIBERS', 'материал от подписчиков'), ('COMPETITION', 'конкурс')], null=True),
        ),
    ]
