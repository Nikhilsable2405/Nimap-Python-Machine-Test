from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name', read_only=True)
    users = UserSerializer(many=True, read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
