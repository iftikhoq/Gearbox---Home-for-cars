# Generated by Django 5.1.3 on 2025-01-26 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_orders_trxid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='quantity',
        ),
    ]
