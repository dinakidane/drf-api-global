from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'date_created', 'date_modified', 'full_name',
            'description', 'profile_image'
        ]
