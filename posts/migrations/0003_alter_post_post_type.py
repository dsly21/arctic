# Generated by Django 4.1.2 on 2022-11-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.TextField(choices=[('FROM_SUBSCRIBERS', 'Sub'), ('COMPETITION', 'Comp'), ("[('FROM_SUBSCRIBERS', 'материал от подписчиков'), ('COMPETITION', 'конкурс')]", 'Post Type Choices')], default='общий пост'),
        ),
    ]
