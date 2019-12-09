from rest_framework import serializers


class ViewsetSerializer(serializers.Serializer):
    """
    Serialize data for viewset test
    """
    name = serializers.CharField(max_length=10)
