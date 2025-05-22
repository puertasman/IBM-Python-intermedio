from django.db import models

# Create your models here.
class Project(models.Model):
    """ Esto es una entidad de la base de datos"""
    title = models.CharField(max_length=200, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField(upload_to = 'projects', verbose_name = 'Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición')
    direccion = models.URLField(max_length=200, verbose_name='Dirección', blank=True, null=True)
    class Meta:
        """ Metadatos de la clase """
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created'] # el guión es inverso

    def __str__(self):
        return self.title
        # en lugar de nombre raro, da el título del proyecto
    
