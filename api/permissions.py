from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a Snippet to edit it.    
    """

    def has_object_permission(self, request, view, obj):
        # Allow read requests such as GET, HEAD or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Compare current user to the object owner, return True if it's the same user
        return obj.owner == request.user