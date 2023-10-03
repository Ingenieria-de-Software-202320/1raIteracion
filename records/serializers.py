from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "phone", "role", "password")
        extra_kwargs = {
            'password': {'write_only': True}, 
        }
