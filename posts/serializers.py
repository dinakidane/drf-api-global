from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Read-only field for the post owner's username
    is_owner = serializers.SerializerMethodField()  # Custom method field to check if the request's user is the owner
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')  # Read-only field for the owner's profile ID
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')  # Read-only field for the profile image URL

    def get_is_owner(self, obj):
        """
        Check if the requesting user is the owner of the post.
        """
        request = self.context.get('request')  # Safely retrieve the request from the context
        return request.user == obj.owner  # Return True if the request user matches the post owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image'
        ]
