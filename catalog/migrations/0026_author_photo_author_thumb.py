# Generated by Django 2.1 on 2018-08-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20180830_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo_author_thumb',
            field=models.CharField(blank=True, max_length=255, verbose_name='Thumbnail image'),
        ),
    ]
