from django.shortcuts import render


from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer
from clients.models import Client
from django.shortcuts import get_object_or_404

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client_id = self.kwargs.get("client_id")
        client = get_object_or_404(Client, id=client_id)
        serializer.save(client=client, created_by=self.request.user)

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)

