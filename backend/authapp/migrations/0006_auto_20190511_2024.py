# Generated by Django 2.1.7 on 2019-05-11 17:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20190511_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giftuser',
            old_name='birhdate',
            new_name='birthdate',
        ),
        migrations.AlterField(
            model_name='giftuser',
            name='active_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 17, 24, 15, 811268, tzinfo=utc)),
        ),
    ]
