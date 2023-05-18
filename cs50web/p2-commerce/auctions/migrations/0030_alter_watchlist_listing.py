# Generated by Django 4.1.7 on 2023-05-12 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_watchlist_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='auctions.listing'),
        ),
    ]
