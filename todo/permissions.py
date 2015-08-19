from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow user to access to
    his objects.
    Assumes model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
