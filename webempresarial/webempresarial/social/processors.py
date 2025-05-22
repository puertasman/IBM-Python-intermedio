""" Procesador para los enlaces """
from .models import Link

def ctx_dict(request):
    """ Contexto de la aplicación """
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
