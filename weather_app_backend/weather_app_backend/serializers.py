from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'first_name']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

