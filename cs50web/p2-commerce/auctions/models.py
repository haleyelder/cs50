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
    
# add to watchlist
class Watchlist(models.Model):
    pass  
    
# auction listings
class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    current_bid = models.IntegerField(null=True)
    image_url = models.CharField(max_length=255,blank=True, null=True)
    category = models.ManyToManyField(Category,related_name='categories')


    def __str__(self):
        return f"{self.title} | Current Bid: {self.current_bid}"
    
# listing comments
class Comment(models.Model):
    text = models.CharField(max_length=255)
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name='comments',null=True)

    def __str__(self):
        return self.text


class Bid(models.Model):
    start_bid = models.IntegerField(null=True)
    current_bid = models.IntegerField(null=True)
    bid_status = models.BooleanField(default=False, null=True)
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name='bids',null=True)

    
    def __str__(self):
        return f"Starting Bid: {self.start_bid}, Current Bid: {self.current_bid}"
