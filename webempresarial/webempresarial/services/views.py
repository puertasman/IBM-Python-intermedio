from .models import Service
from django.shortcuts import render


# Create your views here.

def services(request):
    """ Página servicios """
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})
