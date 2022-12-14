# Generated by Django 4.1.2 on 2022-12-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userfriendinstance_country_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfriendinstance',
            name='country_subject',
        ),
        migrations.RemoveField(
            model_name='userfriendinstance',
            name='locality',
        ),
        migrations.AlterField(
            model_name='userfriendinstance',
            name='postal_address',
            field=models.TextField(help_text='Например Якутская область, город Якутск, ул.Красного знамени, д.19, кв.2', verbose_name='Полный адрес проживания'),
        ),
        migrations.AlterField(
            model_name='userfriendinstance',
            name='social_network_nickname',
            field=models.CharField(blank=True, help_text='Например id222829594', max_length=60, null=True, verbose_name='Укажите как вас найти "вконтакте"'),
        ),
    ]
