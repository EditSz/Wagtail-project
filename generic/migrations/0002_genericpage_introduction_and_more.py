# Generated by Django 4.2.1 on 2023-05-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='banner_title',
            field=models.CharField(default='Welcome to my generic page!', max_length=100),
        ),
    ]
