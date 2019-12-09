from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes data from users models
    """
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
