# Generated by Django 4.1.2 on 2022-12-07 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_userfullinks_alter_contactinformation_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='permission_publish',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
    ]
