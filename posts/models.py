from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    
    image_filter_choices_list = [
        ('clarendon', 'Clarendon'), 
        ('gingham', 'Gingham'),
        ('moon', 'Moon'), 
        ('reyes', 'Reyes'),
        ('perpetua', 'Perpetua'), 
        ('amaro', 'Amaro'),
        ('mayfair', 'Mayfair'), 
        ('willow', 'Willow'),
        ('juno', 'Juno'), 
        ('slumber', 'Slumber'),
        ('crema', 'Crema'), 
        ('ludwig', 'Ludwig'),
        ('aden', 'Aden'), 
        ('brooklyn', 'Brooklyn')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the post to a User
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set the time when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-set the time whenever the post is updated
    title = models.CharField(max_length=255)  # The title of the post
    content = models.TextField(blank=True)  # Post content, optional
    image = models.ImageField(
        upload_to='images/', default='../default_profile_ky9c7z', blank=True  # Optional image with a default fallback
    )

    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices_list, default='normal'
    )

    class Meta:
        ordering = ['-created_at']  # Order posts by the latest created first

    def __str__(self):
        return f'{self.id} {self.title}'  # String representation of the post
