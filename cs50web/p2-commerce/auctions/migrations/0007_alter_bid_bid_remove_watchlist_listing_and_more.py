# Generated by Django 4.2.11 on 2025-02-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_bid_current_bid_remove_bid_start_bid_bid_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(null=1),
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='listing',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing',
            field=models.ManyToManyField(related_name='watchlist', to='auctions.listing'),
        ),
    ]
