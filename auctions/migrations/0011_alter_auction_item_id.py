# Generated by Django 4.1 on 2022-12-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0010_alter_bidding_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auction_item",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]