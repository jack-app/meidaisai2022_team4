# Generated by Django 3.2.13 on 2022-05-28 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 11, 17, 26, 379994, tzinfo=utc)),
        ),
    ]
