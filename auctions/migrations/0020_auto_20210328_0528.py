# Generated by Django 3.1.7 on 2021-03-28 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20210328_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='listing_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='listing_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='listing_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='listing_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='listing_user',
            new_name='user',
        ),
    ]
