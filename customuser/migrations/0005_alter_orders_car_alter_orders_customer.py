# Generated by Django 5.1.3 on 2025-01-26 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_cars_quantity'),
        ('customuser', '0004_remove_orders_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='cars.cars'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
