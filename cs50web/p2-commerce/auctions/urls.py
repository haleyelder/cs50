from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add_auction", views.add_auction, name="add_auction"),
    path("detail/<int:id>/", views.detail, name="detail"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/edit/<int:auction_id>", views.edit_watchlist, name="edit_watchlist"),
    path('category_auction/<int:category_id>/', views.category_auction, name="category_auction"),
]
