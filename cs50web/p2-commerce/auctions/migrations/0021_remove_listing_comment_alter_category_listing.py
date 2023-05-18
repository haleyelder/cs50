# Generated by Django 4.1.7 on 2023-05-08 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_listing_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comment',
        ),
        migrations.AlterField(
            model_name='category',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.listing'),
        ),
    ]