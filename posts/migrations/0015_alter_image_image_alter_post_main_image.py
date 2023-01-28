# Generated by Django 4.1.2 on 2023-01-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_alter_contactinformation_options_alter_image_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте несколько изображений. Внимание: название изображения должно быть на латинице. Пример: image.jpg', null=True, upload_to='posts/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(help_text='Это изображение будет расположено на миниатюре списка публикаций и в самом верху поста. Внимание: название изображения должно быть на латинице. Пример: image.jpg', upload_to='posts/', verbose_name='Главное изображение'),
        ),
    ]