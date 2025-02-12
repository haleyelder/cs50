from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.forms import ModelForm
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.db.models import Max

from .models import User, Auction, Bid, Comment, Category, Watchlist

@login_required
def index(request):
    auctionlist = Auction.objects.all()
    bid = Bid.objects.all()
    highest_num = Bid.objects.values('auction_id').annotate(max_value=Max('bid'))

    if request.user.is_authenticated:
        return render(request, "auctions/index.html", {
            "auctionlist":auctionlist,
            "bid":bid,
            "highest_num":highest_num
        })
    else:
        return render(request, 'auctions/login.html')

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

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
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

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

def add_auction(request):
    if request.method == "POST":
        addform = AddAuction(request.POST)
        if addform.is_valid():
            addform = addform.save(commit=False)
            addform.created_by = User.objects.get(username=request.user)
            addform.save()

        else:
            return render(request, 'auctions/add_auction.html', {
                "addform":addform
            })

    return render(request, 'auctions/add_auction.html', {
        "addform": AddAuction()
    })

class AddAuction(ModelForm):
    class Meta:
        model = Auction
        fields = ['title','description','start_bid','image_url','category']

@login_required
def detail(request, id):
    user = request.user.id
    listing_creator = request.user
    auctions = Auction.objects.get(id=id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    comments = Comment.objects.filter(auction=auctions)
    categories = Category.objects.filter(categories=id)
    bid = Bid.objects.filter(auction=auctions)

    highest_bid = Bid.objects.values('auction_id').annotate(max_value=Max('bid'))
    winning_bid_user = Bid.objects.filter(auction_id=id).order_by('-bid').first()

    if request.method == "POST":
        commentform = AddComment(request.POST)
        bidform = BidForm(request.POST)

    ## add comment to auction
        if commentform.is_valid():
            commentform = commentform.save(commit=False)
            commentform.auction = Auction.objects.get(id=id)
            commentform.created_by = User.objects.get(username=request.user)
            commentform.save()
            return HttpResponseRedirect('/detail/' + str(id))

        else:
            form = AddComment()

        if bidform.is_valid():

            bid = bidform.save(commit=False)
            bid.auction = Auction.objects.get(id=id)
            bid.bid_user = User.objects.get(username=request.user)
            entered_bid = bidform.cleaned_data['bid']

            last_bid = 0
            for max in highest_bid:
                if max['auction_id'] == auctions.id:
                    last_bid = max['max_value']

            if bid.auction.start_bid and last_bid:
                if entered_bid > last_bid:
                    bid.save()
                else:
                    messages.error(request, "Bid must be higher than previous bid")

            elif bid.auction.start_bid:
                if entered_bid > bid.auction.start_bid:
                    bid.save()
                else:
                    messages.error(request, "Bid must be higher than previous bid")

            return HttpResponseRedirect('/detail/' + str(id))

        else:
            bidform = BidForm()

        if request.method == "POST":
            auctions.isActive = False
            auctions.save()
            return HttpResponseRedirect('/')

    else:
        user = None

    return render(request, 'auctions/detail.html', {
        "commentform": AddComment(),
        "listing_creator":listing_creator,
        "auctions":auctions,
        "watchlist":watchlist,
        "categories":categories,
        "comments":comments,
        "bid": bid,
        "winning_bid_user":winning_bid_user,
        "bidform": BidForm(),
    })

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories":categories,
    })

def category_auction(request,category_id):
    auctions = Auction.objects.filter(category__id=category_id)
    name = Category.objects.filter(id=category_id)

    return render(request, "auctions/category_auction.html", {
        "auctions":auctions,
        "name":name
    })

def edit_watchlist(request,auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)

    if auction in watchlist.auctions.all():
        watchlist.auctions.remove(auction)
    else:
        watchlist.auctions.add(auction)

    return HttpResponseRedirect('/detail/' + str(auction_id))

def watchlist(request):
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)

    return render(request, "auctions/watchlist.html", {
        'watchlist': watchlist
    })
