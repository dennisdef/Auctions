# Generated by Django 3.1.7 on 2021-03-29 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_auto_20210330_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]
