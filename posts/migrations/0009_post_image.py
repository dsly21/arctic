# Generated by Django 4.1.2 on 2022-11-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
