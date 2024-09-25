from rest_framework import serializers
from .models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['user', 'subscribed_to']

    def validate(self, attrs):
        # Ensure a user can't subscribe to themselves
        if attrs['user'] == attrs['subscribed_to']:
            raise serializers.ValidationError("You cannot subscribe to yourself.")
        return attrs
