from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit just their own profile"""

    def has_object_permission(self, request, viwe, obj):
        """Check user who trying to change his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
