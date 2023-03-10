# Generated by Django 4.1 on 2022-12-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_alter_auction_item_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bidding",
            name="current_bid",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="bidding",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="listing_item",
                to="auctions.auction_item",
            ),
        ),
    ]
