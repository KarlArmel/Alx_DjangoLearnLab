from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to modify data, but read access for others.
    """
    def has_permission(self, request, view):
        # Allow read-only actions for everyone
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Allow write actions for admin users only
        return request.user and request.user.is_staff
