from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path("<slug>", views.product, name="product"),
]
