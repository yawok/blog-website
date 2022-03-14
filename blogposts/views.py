from django.shortcuts import render

from .models import Post

def index(request):
    """The home page"""
    return render(request, "blogposts/index.html")


def posts(request):
    """Page to display all the posts."""
    posts = Post.objects.order_by("date")
    context = {"posts": posts}
    return render(request, "blogposts/posts.html", context)


def post(request, post_id):
    """Page to display content of a post."""
    title = Post.objects.get(id=post_id)
    content = title.post
    context = {"title": title, "content": content}
    return render(request, "blogposts/post.html", context)
