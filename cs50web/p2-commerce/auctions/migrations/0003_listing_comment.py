# Generated by Django 4.1.7 on 2023-04-29 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_listing_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='comment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.comment'),
        ),
    ]
