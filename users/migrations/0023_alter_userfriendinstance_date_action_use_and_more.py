# Generated by Django 4.1.2 on 2022-11-18 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_userfriendinstance_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfriendinstance',
            name='date_action_use',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 18, 16, 56, 5, 969950, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='userfriendinstance',
            name='user_friends',
            field=models.TextField(blank=True, null=True),
        ),
    ]
