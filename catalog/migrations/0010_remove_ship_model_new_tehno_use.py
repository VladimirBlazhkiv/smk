# Generated by Django 2.1 on 2018-08-16 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180816_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship_model',
            name='new_tehno_use',
        ),
    ]
