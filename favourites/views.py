from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Favourite
from .serializers import FavouriteSerializer
from posts.models import Post

class FavouriteListCreateView(generics.ListCreateAPIView):
    """
    View to list and create favourites.
    """
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        post = get_object_or_404(Post, id=post_id)

        if post.owner == request.user:
            return Response({"error": "You cannot like your own post."}, status=status.HTTP_403_FORBIDDEN)

        # Check if the favourite already exists
        existing_favourite = Favourite.objects.filter(user=request.user, post=post).first()
        if existing_favourite:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)

class FavouriteDetailView(generics.DestroyAPIView):
    """
    View to delete a favourite (unlike a post).
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        post_id = self.kwargs['post_id']
        favourite = get_object_or_404(Favourite, user=self.request.user, post_id=post_id)
        return favourite

    def delete(self, request, *args, **kwargs):
        favourite = self.get_object()
        self.perform_destroy(favourite)
        return Response(status=status.HTTP_204_NO_CONTENT)
