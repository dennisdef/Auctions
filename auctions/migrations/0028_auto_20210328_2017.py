# Generated by Django 3.1.7 on 2021-03-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_auto_20210328_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='default.png', upload_to='auctions/images/'),
        ),
    ]