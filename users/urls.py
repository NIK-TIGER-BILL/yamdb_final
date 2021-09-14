from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, get_confirmation_code, get_token

router = DefaultRouter()
router.register('users', UserViewSet)

authpatterns = [
    path('mail/', get_confirmation_code),
    path('token/', get_token)
]

urlpatterns = [
    path('v1/auth/', include(authpatterns)),
    path('v1/', include(router.urls)),
]
