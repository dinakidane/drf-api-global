from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Favourite(models.Model):
    """
    Model to track which users have liked which posts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favourited_by')

    class Meta:
        unique_together = ('user', 'post')  # Ensure a user can only like a post once

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"

