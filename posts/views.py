from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsProfileOwnerOrReadOnly

class PostListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request): 
        """Retrieve all posts."""
        all_posts = Post.objects.all()
        post_serializer = PostSerializer(all_posts, many=True, context={'request': request})
        return Response(post_serializer.data)

    def post(self, request):
        """Create a new post."""
        new_post_serializer = PostSerializer(data=request.data, context={'request': request})
        if new_post_serializer.is_valid():
            new_post_serializer.save(owner=request.user)
            return Response(new_post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(new_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    permission_classes = [IsProfileOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get_object(self, pk):
        """Retrieve a post by its primary key."""
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """Retrieve a specific post."""
        post = self.get_object(pk)
        post_serializer = PostSerializer(post, context={'request': request})
        return Response(post_serializer.data)

    def put(self, request, pk):
        """Update a specific post."""
        post = self.get_object(pk)
        updated_post_serializer = PostSerializer(post, data=request.data, context={'request': request})
        if updated_post_serializer.is_valid():
            updated_post_serializer.save()
            return Response(updated_post_serializer.data)
        return Response(updated_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a specific post."""
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

