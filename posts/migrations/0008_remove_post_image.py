# Generated by Django 4.1.2 on 2022-11-01 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
