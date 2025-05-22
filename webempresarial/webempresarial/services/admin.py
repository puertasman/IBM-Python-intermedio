from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    """ Configuración del modelo en el admin """
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
