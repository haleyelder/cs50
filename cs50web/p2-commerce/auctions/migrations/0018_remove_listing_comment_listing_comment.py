# Generated by Django 4.1.7 on 2023-05-08 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_listing_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comment',
        ),
        migrations.AddField(
            model_name='listing',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.comment'),
        ),
    ]
