from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """A blog post."""
    title = models.CharField(max_length=256)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.title) > 50:
            return f"{self.title[:50]}..."
        else:
            return self.title
