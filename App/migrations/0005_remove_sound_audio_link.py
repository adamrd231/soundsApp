# Generated by Django 3.2 on 2021-04-29 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210429_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sound',
            name='audio_link',
        ),
    ]
