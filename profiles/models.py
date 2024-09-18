from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to='images/', default='../samples/default_profile_ky9c7z'
    )

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.user.username}'s profile"


def user_profile_creation(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(user_profile_creation, sender=User)

