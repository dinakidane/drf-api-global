from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Subscriber
from .serializers import SubscriberSerializer

class SubscriberListCreateView(generics.ListCreateAPIView):
    """
    View to list current user's subscriptions and to create new subscriptions.
    """
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return subscriptions for the logged-in user
        return Subscriber.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SubscriberDetailView(generics.DestroyAPIView):
    """
    View to unsubscribe from a user's profile.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Get the subscriber relationship
        return get_object_or_404(
            Subscriber,
            user=self.request.user,
            subscribed_to=self.kwargs['subscribed_to_id']
        )

    def delete(self, request, *args, **kwargs):
        subscriber = self.get_object()
        self.perform_destroy(subscriber)
        return Response(status=status.HTTP_204_NO_CONTENT)

