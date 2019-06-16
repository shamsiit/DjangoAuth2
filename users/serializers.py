from rest_framework import serializers
from .models import AppUser


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }