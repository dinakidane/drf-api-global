from rest_framework import serializers
from .models import Favourite
from posts.models import Post

class FavouriteSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = Favourite
        fields = ['id', 'user', 'post']  # You may choose to exclude user from the response
        read_only_fields = ['user']  # User is set from the request

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  # Automatically set user to the logged-in user
        return super().create(validated_data)
