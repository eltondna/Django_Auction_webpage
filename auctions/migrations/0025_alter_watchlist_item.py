# Generated by Django 4.1 on 2022-12-21 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0024_remove_auction_item_watchlist_user_watchlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watchlist",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist_item",
                to="auctions.auction_item",
                unique=True,
            ),
        ),
    ]
