# Generated by Django 3.1.7 on 2021-03-27 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20210328_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
