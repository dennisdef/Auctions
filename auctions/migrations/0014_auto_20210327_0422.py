# Generated by Django 3.1.7 on 2021-03-27 02:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_listing_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
