# Generated by Django 2.1.7 on 2019-05-14 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20190511_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresslist',
            name='user',
        ),
        migrations.AlterField(
            model_name='giftuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 9, 28, 16, 588135, tzinfo=utc)),
        ),
    ]
