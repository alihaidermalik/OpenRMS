# Generated by Django 2.0.2 on 2020-05-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='image',
            field=models.ImageField(unique=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(unique=True, upload_to='pictures'),
        ),
    ]