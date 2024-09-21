from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()  # Method field to check if the current user is the owner

    def get_is_owner(self, obj):
        """
        Check if the request's user is the owner of the profile.
        """
        request = self.context.get('request')  # Safely get the request from the context
        return request.user == obj.user  # Compare the requesting user with the profile owner

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'date_created', 'date_modified', 'full_name',
            'description', 'profile_image', 'is_owner'
        ]
