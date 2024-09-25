from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Reply(models.Model):
    """
    Reply model for users to comment on posts.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']  # Latest replies first

    def __str__(self):
        return f"Reply by {self.owner} on {self.post.title}"

