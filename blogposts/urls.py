"""Defines the url patterns for the app."""

from django.urls import path

from . import views

app_name = "blogposts"
urlpatterns = [
        #home page
        path("", views.index, name="index"),
        #Display all posts
        path("posts/", views.posts, name="posts"),
        #Display the content of a post
        path("posts/<int:post_id>/", views.post, name="post"),
        #Form to add new posts
        path("posts/new_post/", views.new_post, name="new_post"),
        #Form to make edits to posts
        path("posts/edit_post/<int:title_id>/", views.edit_post, name="edit_post")
        ]
