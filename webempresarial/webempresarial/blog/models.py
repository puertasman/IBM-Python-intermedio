from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    """ Categorías de las entradas del blog """
    name = models.CharField(max_length=100, verbose_name = 'Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición')
    
    class Meta:
        """ Metadatos de la clase """
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['created'] # el guión es inverso

    def __str__(self):
        return self.name
        # en lugar de nombre raro, da el nombre de la categoría

class Post(models.Model):
    """ Entradas del blog """
    title = models.CharField(max_length=100, verbose_name = 'Título')
    content = models.TextField(verbose_name = 'Contenidos')
    published = models.DateTimeField(verbose_name = 'Fecha de publiación', default = now)
    image = models.ImageField(upload_to = 'blog', verbose_name = 'Imagen', blank = True, null = True)
    author = models.ForeignKey(User, verbose_name = 'Autor', on_delete = models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name = 'Categorías', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición')
    
    class Meta:
        """ Metadatos de la clase """
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created'] # el guión es inverso

    def __str__(self):
        return self.title
        # en lugar de nombre raro, da el nombre de la categoría
