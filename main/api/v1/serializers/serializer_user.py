import requests
from django.contrib.auth import password_validation
from rest_framework import serializers, request
from main.api.v1.base import reverse_url
from main.models import User, Repository

class UserRetrieveAllLocalReposAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_repositories = UserRetrieveAllLocalReposAPISerializer(many=True, read_only=True)

    class Meta:
            model = User
            fields = ('id_user', 'login', 'node_id', 'user_repositories', 'created_at', 'deleted_in', 'is_deleted',)

