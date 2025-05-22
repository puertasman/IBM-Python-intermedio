from django.contrib import admin
from .models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """ Configuración del modelo en el admin"""
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    """ Configuración del modelo en el admin """
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author','-published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author', 'categories')

    def post_categories(self, obj):
        """ Devuelve las categorías de la entrada """
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    
    post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)