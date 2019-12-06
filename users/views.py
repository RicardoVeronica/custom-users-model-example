from .serializers import HelloSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """
    Test APIView
    """
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """
        Return a list of APIView freatures
        """
        message = 'hello world'
        an_apiview = [
            'Use HTTP methods',
            'Similar to traditional Django views',
            'Give you the most control over your application logic',
            'Mapped manually to your URLs config'
        ]

        # Response return a list or dict
        return Response(
            {
                'message': message,
                'an_apiview': an_apiview
            }
        )

    def post(self, request):
        """
        Create a hello message whit serializers name
        """
        serializer_data = self.serializer_class(data=request.data)

        if serializer_data.is_valid():
            name = serializer_data.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer_data.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """
        Handle updating an object
        """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Handle partial update of an object
        """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Delete an object
        """
        return Response({'method': 'DELETE'})
