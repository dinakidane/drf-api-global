from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsProfileOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow profile owners to edit their profile.
    Read-only access is allowed for any request method that is safe (GET, HEAD, OPTIONS).
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only access for safe methods
        if request.method in SAFE_METHODS:
            return True
        # Only allow access if the user is the owner of the profile
        return obj.user == request.user
