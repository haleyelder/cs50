from django.contrib.auth.models import AbstractUser
from django.db import models

# user auth log in stuff
class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural= "Categories"

    def __str__(self):
        return f"{self.name}"

# auction listings
class Auction(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_bid = models.IntegerField(null=True)
    image_url = models.CharField(max_length=255,blank=True, null=True)
    category = models.ManyToManyField(Category,related_name='categories')
    isActive = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

# listing comments
class Comment(models.Model):
    text = models.CharField(max_length=255)
    auction = models.ForeignKey(Auction,on_delete=models.CASCADE,related_name='comments',null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}, posted by {self.created_by}"

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="watchlist")
    auctions = models.ManyToManyField(Auction, related_name="watched_by", blank=True)

    def __str__(self):
        return f"{self.user.username}'s watchlist"


class Bid(models.Model):
    bid = models.IntegerField(default=0)
    auction = models.ForeignKey(Auction,on_delete=models.CASCADE,related_name='auction')
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bid_user} bid: ${self.bid} on {self.auction}"
