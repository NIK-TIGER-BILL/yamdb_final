from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = bool(request.user and request.user.is_staff)
        return request.method in permissions.SAFE_METHODS or is_admin
