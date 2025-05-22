from django.db import models
from django.forms import SlugField

# Create your models here.
class Link(models.Model):
    """ Enlaces de la página web """
    key = models.SlugField(max_length = 100, verbose_name = 'Nombre clave', unique = True)
    name = models.CharField(max_length = 200, verbose_name = 'Nombre')
    url = models.URLField(max_length = 200, verbose_name = 'Enlace', null = True, blank = True) 
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición')
    
    class Meta:
        """ Metadatos de la clase """
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name'] # el guión es inverso

    def __str__(self):
        return self.name
        # en lugar de nombre raro, da el nombre de la categoría
