# Generated by Django 3.1.7 on 2021-03-29 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_bid_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
    ]
