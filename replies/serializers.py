from rest_framework import serializers
from .models import Reply
from posts.models import Post
from profiles.models import UserProfile

class ReplySerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    profile_id = serializers.ReadOnlyField(source='owner.userprofile.id')  # Add profile ID
    profile_image = serializers.ImageField(source='owner.userprofile.profile_image', allow_null=True)  # Add profile image
    owner = serializers.ReadOnlyField(source='owner.username')  # Add owner field

    class Meta:
        model = Reply
        fields = ['id', 'content', 'created_at', 'updated_at', 'owner', 'post', 'profile_id', 'profile_image']
        
class ReplyDetailSerializer(ReplySerializer):
    """
    Serializer for Reply model used in detail view.
    Includes profile info such as profile id and profile image.
    """
    profile_id = serializers.ReadOnlyField(source='owner.userprofile.id')
    profile_image = serializers.ImageField(source='owner.userprofile.profile_image')

    class Meta:
        model = Reply
        fields = ReplySerializer.Meta.fields + ['profile_id', 'profile_image']
