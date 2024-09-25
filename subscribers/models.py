from django.db import models
from django.contrib.auth.models import User

class Subscriber(models.Model):
    """
    Model to manage subscriptions between users.
    """
    user = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'subscribed_to')  # Prevent duplicate subscriptions

    def __str__(self):
        return f"{self.user.username} subscribed to {self.subscribed_to.username}"

