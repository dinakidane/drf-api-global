from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from drf_api.permissions import IsProfileOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class UserProfileListView(APIView):
    """
    Retrieve a list of all user profiles.
    Profile creation is managed by Django signals, so no POST method required.
    """
    def get(self, request):
        user_profiles = UserProfile.objects.all()
        serialized_profiles = UserProfileSerializer(
            user_profiles, many=True, context={'request' : request}
        )
        return Response(serialized_profiles.data)

class UserProfileDetailView(APIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            user_profile = UserProfile.objects.get(pk=pk)
            self.check_object_permissions(self.request, user_profile)
            return user_profile
        except UserProfile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(
            user_profile, context={'request' : request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(
            user_profile, data=request.data, context={'request' : request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

