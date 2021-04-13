from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """User Permission class."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
