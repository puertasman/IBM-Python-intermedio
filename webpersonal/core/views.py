from django.shortcuts import render, HttpResponse
# devuelve a una petición con un código

# Create your tests here.
# Vistas, lógica que se ejecuta al hacer una petición a una URL

def home(request):
    """Página inicial"""
    return render(request, 'core/home.html')

def about(request):
    """ Página de informació personal """
    return render(request, 'core/about-me.html')

def portfolio(request):
    """ Página de portfolio """
    return render(request, 'core/portfolio.html')

def contacto(request):
    """ Página de contacto """
    return render(request, 'core/contacto.html')
 