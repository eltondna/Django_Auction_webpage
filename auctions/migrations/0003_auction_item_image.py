# Generated by Django 4.1 on 2022-12-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0002_auction_item_bidding"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction_item",
            name="image",
            field=models.ImageField(null=True, upload_to="image/"),
        ),
    ]