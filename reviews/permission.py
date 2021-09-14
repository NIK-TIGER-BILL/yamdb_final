from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import UserRole


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user


class IsAdminOrModerUser(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and (
                request.method in SAFE_METHODS
                or request.user.is_staff
                or request.user.role == UserRole.ADMIN
                or request.user.role == UserRole.MODERATOR
            )
        )
