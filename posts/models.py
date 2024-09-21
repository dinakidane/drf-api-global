from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the post to a User
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set the time when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-set the time whenever the post is updated
    title = models.CharField(max_length=255)  # The title of the post
    content = models.TextField(blank=True)  # Post content, optional
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True  # Optional image with a default fallback
    )

    class Meta:
        ordering = ['-created_at']  # Order posts by the latest created first

    def __str__(self):
        return f'{self.id} {self.title}'  # String representation of the post
