from django.urls import path
from .views import UserAPIView, DetailUser

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', DetailUser.as_view())
]
