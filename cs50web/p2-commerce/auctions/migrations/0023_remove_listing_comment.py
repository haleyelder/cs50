# Generated by Django 4.1.7 on 2023-05-08 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_listing_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comment',
        ),
    ]