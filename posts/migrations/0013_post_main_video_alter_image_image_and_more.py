# Generated by Django 4.1.2 on 2022-12-11 13:17

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_video',
            field=embed_video.fields.EmbedVideoField(blank=True, help_text='Видео будет расположено на верху страницы поста. Добавлять сюда видео нужно, когда видео ролик - это основной, заглавный контент поста.', null=True, verbose_name='главное видео'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте несколько изображений', null=True, upload_to='posts/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(help_text='Это изображение будет расположено на миниатюре списка публикаций и в самом верху поста.', upload_to='posts/', verbose_name='Главное изображение'),
        ),
    ]