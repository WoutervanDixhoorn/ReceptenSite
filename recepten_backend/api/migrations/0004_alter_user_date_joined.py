# Generated by Django 3.2.5 on 2022-05-04 12:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2022, 5, 4, 12, 29, 32, 8581, tzinfo=utc)),
        ),
    ]