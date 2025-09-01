from django.db import models
from django.contrib.auth.models import User
from clients.models import Client

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name="projects", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="assigned_projects")
    created_by = models.ForeignKey(User, related_name="created_projects", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

