from django.contrib.auth import authenticate
from rest_framework import serializers
from backend.status_code import STATUS_MESSAGES

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if user is None:
            raise serializers.ValidationError(f'{STATUS_MESSAGES["errors"]["INVALID_CREDENTIALS"]}')
        return user
