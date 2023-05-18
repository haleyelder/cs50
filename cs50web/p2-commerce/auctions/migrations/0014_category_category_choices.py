# Generated by Django 4.1.7 on 2023-05-07 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_alter_comment_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_choices',
            field=models.CharField(choices=[('utility', 'Utility'), ('clothing', 'Clothing'), ('sword/armor', 'Sword/Armor'), ('relic', 'Relic')], max_length=25, null=True),
        ),
    ]