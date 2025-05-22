from django.shortcuts import render

# Create your views here.

def home(request):
    """ Página inicial """
    return render(request, 'core/home.html')

def about(request):
    """ Página sobre nosotros """
    return render(request, 'core/about.html')

def store(request):
    """ Página tienda """
    return render(request, 'core/store.html')
