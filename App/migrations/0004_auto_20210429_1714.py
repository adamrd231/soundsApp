# Generated by Django 3.2 on 2021-04-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210421_1820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Location'},
        ),
        migrations.AlterModelOptions(
            name='sound',
            options={'verbose_name_plural': 'Sound'},
        ),
        migrations.AddField(
            model_name='sound',
            name='sound_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
