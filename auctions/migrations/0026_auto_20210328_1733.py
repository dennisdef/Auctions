# Generated by Django 3.1.7 on 2021-03-28 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_listing_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['date'], 'verbose_name': 'Listing', 'verbose_name_plural': 'Listings'},
        ),
    ]
