from rest_framework import serializers

from ...models import UserProfile
from ...serializers import CreateUserSerializer


class UserProfileOutputSerializer(serializers.Serializer):
    uuid = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    user = CreateUserSerializer()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)
    age = serializers.IntegerField()

class UserProfileCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)
    age = serializers.IntegerField()