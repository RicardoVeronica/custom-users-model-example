from rest_framework import viewsets
from rest_framework.response import Response


class HelloViewSet(viewsets.ViewSet):
    """
    Test API ViewSet
    """
    def list(self, request):
        """
        Retrieve a list of viewsets features
        """
        a_viewset = [
            'Uses actions (list, create, retrieve, update and partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'a_viewset': a_viewset, 'message': 'Hello world!!!'})
