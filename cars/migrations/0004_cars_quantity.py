# Generated by Django 5.1.5 on 2025-01-22 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
