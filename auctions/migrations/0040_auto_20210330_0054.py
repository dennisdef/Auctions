# Generated by Django 3.1.7 on 2021-03-29 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_remove_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
