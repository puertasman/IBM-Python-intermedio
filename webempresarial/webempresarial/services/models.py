from django.db import models

# Create your models here.

class Service(models.Model):
    """ Esto es una entidad de la base de datos"""
    title = models.CharField(max_length=200, verbose_name = 'Título')
    subtitle = models.CharField(max_length=200, verbose_name = 'Subtítulo')
    content = models.TextField(verbose_name = 'Contenido')
    image = models.ImageField(upload_to = 'services', verbose_name = 'Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición')
    
    class Meta:
        """ Metadatos de la clase """
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created'] # el guión es inverso

    def __str__(self):
        return self.title
        # en lugar de nombre raro, da el título del proyecto