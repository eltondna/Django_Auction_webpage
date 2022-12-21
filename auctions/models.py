from django.contrib.auth.models import AbstractUser
from django.db import models




#User data model
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.username}"

###############   Auction data model   #################


# Item description 
class Auction_item(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    creation_date = models.DateTimeField(null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller", null=True)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50,null=True)
    starting_bid = models.IntegerField()
    current_bid = models.IntegerField(null=True)
    creation_date = models.DateTimeField()
    image = models.ImageField(null = True, blank = True,upload_to="image/")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Category: {self.category} Title: {self.title} Starting bid: {self.starting_bid} "

# Bidding condition 
class bidding(models.Model):
    bidder = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bidder",null=True)
    item = models.ForeignKey(Auction_item, on_delete=models.CASCADE, related_name="listing_item",null=False)
    bid_price = models.IntegerField(null=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)



# Watchlist
class Watchlist(models.Model):
    watcher = models.ForeignKey(User,on_delete=models.CASCADE,related_name="watchlist_user")
    item = models.ForeignKey(Auction_item,on_delete=models.CASCADE,related_name="watchlist_item",unique=True)
# Comment







