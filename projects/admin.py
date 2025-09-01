from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'get_client_name')  
    list_filter = ('client',)
    search_fields = ('project_name',)

    def get_client_name(self, obj):
        return obj.client.client_name
    get_client_name.short_description = 'Client Name'
