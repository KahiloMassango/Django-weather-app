# Generated by Django 4.1.7 on 2023-03-13 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
    ]
