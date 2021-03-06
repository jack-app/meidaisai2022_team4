# Generated by Django 3.2.13 on 2022-06-06 02:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_display_name'),
        ('timeline', '0008_auto_20220606_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 6, 2, 13, 18, 422180, tzinfo=utc), help_text='日付'),
        ),
    ]
