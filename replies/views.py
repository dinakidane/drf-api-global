from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_api.permissions import IsProfileOwnerOrReadOnly
from .models import Reply
from .serializers import ReplySerializer, ReplyDetailSerializer

class ReplyList(generics.ListCreateAPIView):
    """
    List all replies or create a new reply if authenticated.
    The perform_create method associates the reply with the logged-in user.
    """
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a reply, or update or delete it by ID if the user is the owner.
    """
    queryset = Reply.objects.all()
    serializer_class = ReplyDetailSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]

    def get_object(self):
        reply = get_object_or_404(Reply, pk=self.kwargs['pk'])
        return reply

                                                                                            