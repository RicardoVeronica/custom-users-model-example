from django.views.generic import ListView
from .models import User


class UserListView(ListView):
    """
    Retrieve a list of users
    """
    model = User
    template_name = 'user_list.html'
