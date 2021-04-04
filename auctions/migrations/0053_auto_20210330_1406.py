# Generated by Django 3.1.7 on 2021-03-30 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0052_comment_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='price',
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]