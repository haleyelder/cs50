from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse

from .models import User, Listing, Bid, Comment, Category,Watchlist

#home page listings
def index(request):
    listinglist = Listing.objects.all()
    

    return render(request, "auctions/index.html", {
        "listinglist":listinglist,
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

# form add listing
def add_listing(request):

    if request.method == "POST":
        addform = AddListing(request.POST)
        if addform.is_valid():
            addform.save()

        else:
            return render(request, 'auctions/add_listing.html', {
                "addform":addform
            })  
              
    return render(request, 'auctions/add_listing.html', {
        "addform": AddListing()
    })  

class AddListing(ModelForm):

    class Meta:
        model = Listing
        fields = ['title','description','current_bid','image_url','category']
    

def detail(request, id):
    listings = Listing.objects.get(id=id)

    #listing is from the model setup
    comments = Comment.objects.filter(listing=listings)
    categories = Category.objects.filter(categories=id)

    if request.method == "POST":
        form = AddComment(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.listing = Listing.objects.get(id=id)
            comment.save()

            return HttpResponseRedirect('/detail/' + str(id))
     
        else:
            form = AddComment()         

    return render(request, 'auctions/detail.html', {
        "form": AddComment(),
        "listings":listings,
        "categories":categories,
        "comments":comments,
    })  

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']



def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories":categories,
    })

def category_listing(request,category_id):
    listings = Listing.objects.filter(category__id=category_id)
    name = Category.objects.filter(id=category_id)

    return render(request, "auctions/category_listing.html", {
        "listings":listings,
        "name":name
    })


def watchlist(request):
    return render(request, "auctions/watchlist.html")