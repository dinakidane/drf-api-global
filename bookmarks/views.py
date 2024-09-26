from rest_framework import generics, permissions
from .models import Bookmark
from .serializers import BookmarkSerializer

class BookmarkListCreateView(generics.ListCreateAPIView):
    """
    List all bookmarks of the logged-in user or add a bookmark to a post.
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookmarkDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a bookmark (removes it).
    """
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)
