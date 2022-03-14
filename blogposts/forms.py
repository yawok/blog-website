from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    """Form to make new posts."""
    class Meta:
        model = Post
        fields = ["title", "post"]
        labels = {"title": "Title", "post": "Content"}


