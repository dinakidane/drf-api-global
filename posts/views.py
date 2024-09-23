from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsProfileOwnerOrReadOnly


class PostView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_posts = Post.objects.all()
        post_serializer = PostSerializer(all_posts, many=True, context={'request': request})
        return Response(post_serializer.data)

    def post(self, request):
        new_post_serializer = PostSerializer(data=request.data, context={'request': request})
        if new_post_serializer.is_valid():
            new_post_serializer.save(owner=request.user)
            return Response(new_post_serializer.data, status=status.HTTP_201_CREATED)
        return Response(new_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
