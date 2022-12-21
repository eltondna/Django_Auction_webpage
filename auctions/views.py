from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User ,Auction_item, bidding, Watchlist

from datetime import datetime


# Main Page
def index(request):
    if request.method == "GET":
        # Display all the 'Active' listing item
        # Extract all active items 
        active_items = Auction_item.objects.filter(active=True)
        return render(request, "auctions/index.html",{
            "active_items": active_items,
        })

# Add Item to Watchlist
@login_required(login_url='login')
def watchlist(request):
    if request.method == "GET":
        watchlist = Watchlist.objects.filter(watcher=request.user)
        return render(request, "auctions/watchlist.html",{
            "watchlist": watchlist,
        })

    else:
        item_id = request.POST.get("id")
        item = Auction_item.objects.get(id=item_id)
        try: 
            w_item = Watchlist(watcher=request.user,item=item)
            w_item.save()
        except IntegrityError:
            pass
        return HttpResponseRedirect(reverse("item_info",args=(item_id)))
    
# Create a listing
@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        # Get bid item information #
        user = request.user
        category = request.POST.get("category")
        image = request.FILES.get("image")
        title = request.POST.get("title")
        description = request.POST.get("description")
        starting_bid = request.POST.get("starting_bid")            
        # Get current datetime 
        creation_date = datetime.now().strftime("%Y-%m-%d %I:%M")
        
        # Save item into Auction item database
        auction_item = Auction_item(creation_date=creation_date, seller=user,category=category,title=title,description=description,image=image,starting_bid=starting_bid,current_bid=starting_bid)
        auction_item.save()
        
        # Import item to the public auction database
        return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/create.html")


#Item Detail Page
@login_required(login_url='login')
def item_info(request,item_id):
    item = Auction_item.objects.get(id=item_id)
    bid_info = bidding.objects.filter(item=item)
    leading_bid = False 
    is_seller = False
############### for "leading_bid" ###############
    # Get number of bid to the item 
    Number_of_bid =len(bid_info)
    # Update bidding information to Login user
    for bid in bid_info:
        if bid.bid_price == item.current_bid:
    # Check whether user's bid is the leading one 
            if bid.bidder == request.user:
                leading_bid = True
                break
################################################

############### for "is_seller" ################
    if item.seller == request.user:
        is_seller = True
################################################
    message = ""
    if request.method == "GET":
        return render(request, "auctions/item_info.html",{
            "item": item,
            "message": message,
            "number_of_bid": Number_of_bid,
            "leading_bid": leading_bid,
            "is_seller": is_seller,
        })
    else:
        new_bid_price = int(request.POST.get("bid_price"))
        # 1. Check whether current bid exists
        # - Compare with starting bid 
        if new_bid_price > int(item.starting_bid):
        # - Compare with current bid price
            if new_bid_price > int (item.current_bid):
                item.current_bid = new_bid_price
                item.save()
        # - Requirement met: Add current new bid_price data
                bid_info = bidding(item=item, bidder=request.user,bid_price = new_bid_price)
                bid_info.save()
                Number_of_bid+=1
                leading_bid = True
            else:
                message = "Bid Price must be greater than current bid"
        else:    
            message = "Bid Price must be greater than starting bid"

        return render(request, "auctions/item_info.html",{
            "item": item,
            "message": message,
            "number_of_bid": Number_of_bid,
            "leading_bid": leading_bid,
        })

#Close listing item (For Seller)
@login_required(login_url='login')
def close(request):
    pass




def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
