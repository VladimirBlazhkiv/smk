# Generated by Django 2.1 on 2018-08-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20180816_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship_model',
            name='ship_prototype',
            field=models.CharField(default=1, help_text='Название прототпа', max_length=200, verbose_name='Прототип'),
            preserve_default=False,
        ),
    ]
