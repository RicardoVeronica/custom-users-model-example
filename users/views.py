from . import serializers
from rest_framework import status, viewsets
from rest_framework.response import Response


class HelloViewSet(viewsets.ViewSet):
    """
    Test API ViewSet
    """
    serializer_class = serializers.ViewsetSerializer

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

    def create(self, request):
        """
        Post method in viewsets
        """
        serializer_data = self.serializer_class(data=request.data)

        if serializer_data.is_valid():
            name = serializer_data.validated_data.get('name')
            message = f'Hello {name}!!'

            return Response({'message': message})
        else:
            return Response(
                serializer_data.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """
        Handle getting an object by its ID
        """
        return Response({'http_method', 'GET'})

    def update(self, request, pk=None):
        """
        Handle updating an objec
        """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """
        Handle updating part of an object
        """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """
        Delete an object
        """
        return Response({'http_method': 'DELETE'})
