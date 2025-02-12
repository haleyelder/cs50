from django.contrib import admin
from .models import User, Auction, Bid, Comment, Category, Watchlist

# class AuctionsAdmin(admin.ModelAdmin):
#     list_display = ('title','description','current_bid')


admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Watchlist)
