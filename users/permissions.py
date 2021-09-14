from rest_framework import permissions

from users.models import UserRole


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff or request.user.role == UserRole.ADMIN:
            return True
