from . import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, base_name='viewset_url')

urlpatterns = [
    path('', include(router.urls))
]
