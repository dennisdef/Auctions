# Generated by Django 3.1.7 on 2021-03-28 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20210328_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
