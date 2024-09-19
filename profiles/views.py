from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileListView(APIView):
    """
    Retrieve a list of all user profiles.
    Profile creation is managed by Django signals, so no POST method required.
    """
    def get(self, request):
        user_profiles = UserProfile.objects.all()
        serialized_profiles = UserProfileSerializer(user_profiles, many=True)
        return Response(serialized_profiles.data)

