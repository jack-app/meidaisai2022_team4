# Generated by Django 3.2.13 on 2022-05-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='display_name',
            field=models.CharField(max_length=100),
        ),
    ]
