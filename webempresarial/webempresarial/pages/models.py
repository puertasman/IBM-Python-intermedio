from django.db import models
from django.forms import SlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    """ Enlaces de la página web """
    title = models.CharField(max_length = 200, verbose_name = 'Título')
    content = RichTextField(verbose_name = 'Contenido')
    order = models.SmallIntegerField(default = 0, verbose_name = 'Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición')
    
    class Meta:
        """ Metadatos de la clase """
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
        ordering = ['order', 'title'] # el guión es inverso

    def __str__(self):
        """ Devuelvel el título para la base de datos """
        return self.title
        # en lugar de nombre raro, da el nombre de la categoría
