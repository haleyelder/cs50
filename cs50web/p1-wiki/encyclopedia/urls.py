from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="title"),
    path('add', views.add, name='add'),
    path("randompage", views.randompage, name="randompage"),
    path('search', views.search, name="search"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
]

