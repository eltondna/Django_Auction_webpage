from django.contrib import admin
from . models import User, Auction_item, bidding,Watchlist
# Register your models here.

admin.site.register(User)
admin.site.register(Auction_item)
admin.site.register(bidding)
admin.site.register(Watchlist)




