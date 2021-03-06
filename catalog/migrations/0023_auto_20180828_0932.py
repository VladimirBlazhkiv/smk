# Generated by Django 2.1 on 2018-08-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20180828_0715'),
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
            field=models.CharField(blank=True, choices=[('---', 'Класс модели не оперделен'), ('F2A', 'F2-A - масштабные копийные модели, длина которых не превышает 900 мм'), ('F2B', 'F2-B - масштабные копийные модели, длина которых составляет от 901 до 1400\xa0мм '), ('F2С', 'F2-C - масштабные копийные модели, длина которых не менее 1401\xa0мм '), ('F2S', 'F2-S - масштабные копийные модели подводных лодок'), ('Ф2Ю', 'Ф2-Ю - Масштабные копийные модели, длина которых не превышает 600 мм'), ('F4А', 'F4-A - Модели, выполненные из любых наборов или полностью готовые'), ('F4B', 'F4-B - модели, выполненные из композитных наборов, которые проходят и стендовую, и ходовую оценки.'), ('F4С', 'F4-C - модели, выполненные из пластмассы, литой под давлением, которые должны проходить и стендовую, и ходовую оценки.'), ('FDS', 'F-DS - точные радиоуправляемые модели - копии паровых кораблей, судов и катеров'), ('NSS-A', 'NSS-A масштабные копийные модели c парусным вооружением типа - бермудский шлюп'), ('NSS-B', 'NSS-B масштабные копийные модели c парусным вооружением типа - гафельный парус'), ('NSS-С', 'NSS-C масштабные копийные модели c парусным вооружением типа - прямые паруса'), ('NSS-D', 'NSS-D масштабные копийные модели - много корпусные парусники')], default='---', help_text='Класс по NAVIGA', max_length=30, verbose_name='NAVIGA Класс'),
        ),
    ]
