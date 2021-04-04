from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import pickle
from django import forms
import datetime
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import messages



def index(request):
    listing = Listing.objects.filter(active=True)
    return render(request, "auctions/index.html", {
        "listings": listing,
    })


def closed_listings(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(active=False),
        "operator": "close",
    })
    
@login_required
def watchlist(request):
    if (request.method == "POST"):
        user = User.objects.get(id = request.POST['user_id'])
        listings = Listing.objects.filter(watchlist = user, active = True)
        return render(request, "auctions/index.html",{
            "listings": listings,
            "operator": "watch"
        })

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


@login_required(redirect_field_name='login')
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


@login_required(redirect_field_name='login')
def create_listing(request):
    return render(request, "auctions/create_listing.html", {
        "categories": Category.objects.all()
    })


@login_required(redirect_field_name='login')
def submit_listing(request):
    if(request.method == "POST"):
        if (request.POST["listing"] == ''):
            messages.error(request, 'Listing description is empty')
            return HttpResponseRedirect(reverse('create_listing'))
        else:
            listing = Listing(title=request.POST["title"], category=Category.objects.get(category=request.POST["category"]),price = request.POST["price"],
                            listing=request.POST["listing"], user=User.objects.get(username=request.POST["owner"]), date=datetime.datetime.now())
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                listing.image = form.cleaned_data['image']
            listing.save()
            new_bid = Bid(post = listing, name=User.objects.get(username=request.POST["owner"]), price = request.POST["price"] )
            new_bid.save()
    return HttpResponseRedirect(reverse('index'))


def listing_page(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    comments = listing.comments.all()
    bids = listing.bids.all()
    highest_bid = listing.bids.order_by("-price").first()
    if (request.method == 'POST'):
        comment_form = CommentForm(data=request.POST)
        comment_user = User.objects.get(username=request.POST["owner"])
        if comment_form.is_valid():
            new_comment = Comment(post=listing, name=comment_user,
                                  comment=comment_form.cleaned_data['comment'], created_on=datetime.datetime.now())
            new_comment.save()

    comment_form = CommentForm()
    watchlist_users = listing.watchlist.all()  
    operator = False
    
    for user in watchlist_users:
        if (user == request.user):
            operator = True

    return render(request, "auctions/listing_page.html", {
        "listing": listing,
        'comments': comments,
        'comment_form': comment_form,
        'bids':bids,
        'highest_bid': highest_bid,
        "operator": operator,
    })


def select_categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })


def category(request, category):
    category = Category.objects.get(category=category)
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(category=category,active=True)
    })


@login_required(redirect_field_name='login')
def close_listing(request):
    if(request.method == "POST"):
        listing_id = request.POST["listing"]
        listing = get_object_or_404(Listing, id=listing_id, user=request.user)
        listing.active = False
        listing.save()
    return HttpResponseRedirect(reverse('listing_page', args=[listing_id]))


@login_required(redirect_field_name='login')
def place_bid(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if (request.method == 'POST'):
        bid_form = BidForm(request.POST)
        if bid_form.is_valid():
            bid = bid_form.cleaned_data["bid"]
            max_bid = listing.bids.order_by('-price').first()
            if (bid > max_bid.price):
                new_bid = Bid(post=listing, name=User.objects.get(
                    username=request.POST["bider"]), price=bid)
                new_bid.save()
                listing.price=bid
                listing.save()
                messages.success(request, 'Bid submitted correctly')
            else:  messages.error(request, 'Warning: Your bid is invalid')

    return HttpResponseRedirect(reverse('listing_page', args=[listing_id]))

@login_required
def add_to_watchlist(request):
    if (request.method == 'POST'):
        listing = get_object_or_404(Listing, id = request.POST["listing"])
        user = User.objects.get(id=request.POST['user'])
        user.in_watchlist.add(listing)
        user.save()
        listing.save()
        return HttpResponseRedirect(reverse('listing_page', args=[request.POST["listing"]]))

@login_required
def remove_from_watchlist(request):
    if (request.method == 'POST'):
        listing = get_object_or_404(Listing, id = request.POST["listing"])
        user = User.objects.get(id=request.POST['user'])
        user.in_watchlist.remove(listing)
        user.save()
        listing.save()
        return HttpResponseRedirect(reverse('listing_page', args=[request.POST["listing"]]))