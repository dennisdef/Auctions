# Generated by Django 3.1.7 on 2021-03-30 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0051_auto_20210330_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
