from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
    style={'input_type': 'password'}
)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'about', 'avatar']
