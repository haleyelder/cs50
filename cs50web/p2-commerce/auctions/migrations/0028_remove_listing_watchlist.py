# Generated by Django 4.1.7 on 2023-05-12 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_watchlist_listing_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
    ]
