# Generated by Django 4.1.2 on 2022-11-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.TextField(choices=[('материал от подписчиков', 'Subscribers'), ('конкурс', 'Competition'), ('общий пост', 'Base Post'), ('пост с ссылкой', 'Link Post')], default='общий пост'),
        ),
    ]
