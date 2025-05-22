from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    """ Página de portfolio """
    projects = Project.objects.all()
    # consulta a la base de datos y añade a la lista

    return render(request, 'portfolio/portfolio.html', {'projects': projects})

 