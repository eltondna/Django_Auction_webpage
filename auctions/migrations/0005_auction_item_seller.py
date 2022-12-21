# Generated by Django 4.1 on 2022-12-18 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "auctions",
            "0004_remove_auction_item_close_remove_auction_item_name_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="auction_item",
            name="seller",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seller",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]