from django.contrib import admin
from .models import Link

# Register your models here.
class linkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return self.readonly_fields
        
admin.site.register(Link, linkAdmin)
