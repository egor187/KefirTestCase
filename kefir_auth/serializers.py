from rest_framework import serializers

from users.models import KefirUser


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = KefirUser
        user = KefirUser()
        fields = ["username", "password"]


class LogoutSerializer(LoginSerializer):
    pass
