"""Defines the url patterns for the app."""

from django.urls import path

from . import views

app_name = "blogposts"
urlpatterns = [
        #home page
        path("", views.index, name="index"),

        ]
