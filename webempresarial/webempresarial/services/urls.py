from . import views as services_views
from django.urls import path

urlpatterns = [
    path('', services_views.services, name='services'),
]