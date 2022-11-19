# Generated by Django 4.1.2 on 2022-11-17 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(40)], verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='arctic_region_flag',
            field=models.BooleanField(help_text='Нажмите, если вы живёте в одном из регионов арктической зоны России (Список регионов)', verbose_name='арктический регион'),
        ),
    ]
