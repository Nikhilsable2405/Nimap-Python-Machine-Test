from rest_framework import serializers
from .models import Client
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'updated_at', 'created_by', 'projects']
