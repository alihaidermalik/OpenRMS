# Generated by Django 2.0.2 on 2020-05-01 08:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0004_auto_20200501_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertype',
            name='name',
            field=models.CharField(choices=[('takeAway', 'Take away'), ('dineIn', 'Dine in'), ('homeDelivery', 'Home delivery')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]