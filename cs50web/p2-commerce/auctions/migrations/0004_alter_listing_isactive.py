# Generated by Django 4.2.11 on 2024-11-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
