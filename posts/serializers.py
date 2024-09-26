from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # Read-only field for the post owner's username
    is_owner = serializers.SerializerMethodField()  # Custom method field to check if the request's user is the owner
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')  # Read-only field for the owner's profile ID
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')  # Read-only field for the profile image URL
    bookmarks_count = serializers.SerializerMethodField()



    def check_image_constraints(self, image_file):
        # Define new limits: 2.5MB for size, 4200px for dimensions
        size_limit = 2.5 * 1024 * 1024  # 2.5MB
        dimension_limit = 4200  # 4200px max height or width

        # Ensure the file size is within the limit
        if image_file.size > size_limit:
            raise serializers.ValidationError('The image exceeds the size limit of 2.5MB.')

        # Ensure the image dimensions are within the allowed range
        if image_file.image.height > dimension_limit:
            raise serializers.ValidationError('Image height cannot exceed 4200px.')
        if image_file.image.width > dimension_limit:
            raise serializers.ValidationError('Image width cannot exceed 4200px.')

        return image_file

    def validate_image(self, value):
        """Validate the image against the defined constraints."""
        self.check_image_constraints(value)
        return value

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
            'title', 'content', 'image', 'image_filter','bookmarks_count',
        ]

    def get_bookmarks_count(self, obj):
        return obj.bookmarked_by.count()

