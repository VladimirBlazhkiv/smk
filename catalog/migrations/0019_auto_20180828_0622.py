# Generated by Django 2.1 on 2018-08-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20180828_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo_author',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Ваше фото'),
        ),
        migrations.AlterField(
            model_name='ship_model',
            name='ship_class_naviga',
            field=models.CharField(blank=True, choices=[('---', 'Класс модели копии не оперделен'), ('F2A', 'Модель копия до 500 мм'), ('F2B', 'Модель копия до 750 мм'), ('F2С', 'Модель копия до 1600 мм'), ('F4А', 'Модель копия '), ('F4B', 'Модель копия '), ('F4С', 'Модель копия '), ('FDS', 'Модель копия с паровым двигателем'), ('NSS-A', 'Парусная модель копия - бермудский парус'), ('NSS-B', 'Парусная модель копия - гафельный парус'), ('NSS-С', 'Парусная модель копия - прямые паруса'), ('NSS-D', 'Парусная модель копия - много корпусные парусники')], default='---', help_text='Класс по NAVIGA', max_length=30, verbose_name='NAVIGA Класс'),
        ),
    ]
