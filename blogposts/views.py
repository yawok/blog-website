from django.shortcuts import render


def index(request):
    """The home page"""
    return render(request, "blogposts/index.html")
