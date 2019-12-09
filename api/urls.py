from django.urls import path
from .views import UserList, UserListCreate

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserListCreate.as_view()),
    # path('users/<int:pk>/', DetailUserListCreate.as_view()),
]
