# Generated by Django 3.1.7 on 2021-03-27 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210327_0422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]