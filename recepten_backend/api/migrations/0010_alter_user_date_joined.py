# Generated by Django 3.2.5 on 2022-05-05 16:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220505_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 16, 17, 18, 970473, tzinfo=utc)),
        ),
    ]
