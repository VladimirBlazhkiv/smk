# Generated by Django 2.1 on 2018-09-02 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_auto_20180830_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship_model',
            name='date_end',
        ),
    ]