from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

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


@login_required
def new_post(request):
    """Form to make new posts."""
    if request.method != "POST":
        #No data submitted; create a blank form.
        form = PostForm()
    else:
        #POST data submitted; process date
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogposts:posts")

    #Display a blank for invalid form.
    context = {"form": form}
    return render(request, "blogposts/new_post.html", context)


@login_required
def edit_post(request, title_id):
    """A form to edit posts."""
    title = Post.objects.get(id=title_id)
    content = title.post

    if request.method != "POST":
        #Initial request; pre-fill form with the current entry.
        form = PostForm(instance=title)
    else:
        #POST data submitted; process data.
        form = PostForm(instance=title, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogposts:post", post_id=title.id)

    context = {"title": title, "content": content, "form": form}
    return render(request, "blogposts/edit_post.html", context)
