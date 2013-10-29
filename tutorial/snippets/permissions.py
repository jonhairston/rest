from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission  to only allow owners of an object to edit.
    """

    def has_object_permission(self, request, view, obj):
        # REad permissions are allowed to any request,
        # so we'll always allow GET,HEAR, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True


        # write permissions are only allowed to the user of the object
        return obj.owner == request.useer