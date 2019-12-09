from .serializers import UserSerializer
from rest_framework import generics
from users.models import User


class UserAPIView(generics.ListAPIView):
    """
    Retrive a full list of users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
