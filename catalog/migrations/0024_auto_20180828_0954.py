# Generated by Django 2.1 on 2018-08-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20180828_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship_model',
            name='ship_scale',
            field=models.CharField(help_text='В каком масштабе вполнена модель', max_length=5, verbose_name='Масштаб 1:'),
        ),
    ]