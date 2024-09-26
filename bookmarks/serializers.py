from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'user_username', 'post', 'post_title', 'created_at']
        read_only_fields = ['user', 'user_username', 'created_at']