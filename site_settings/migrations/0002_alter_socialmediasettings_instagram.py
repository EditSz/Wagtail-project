# Generated by Django 4.2.1 on 2023-05-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]