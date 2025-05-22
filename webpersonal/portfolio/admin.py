from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    """ Configuración del modelo en el admin """
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)
