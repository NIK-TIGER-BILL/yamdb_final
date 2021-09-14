from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class CodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Этот адрес почты уже используется')])
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Это имя пользователя уже используется')])

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'role', 'bio', 'id'
        )
