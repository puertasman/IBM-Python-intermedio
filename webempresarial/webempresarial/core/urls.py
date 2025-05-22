from . import views as core_views
from django.urls import path

urlpatterns = [
    path('', core_views.home, name='home'),
    path('sobre-nosotros/', core_views.about, name='about'),
    path('visitanos/', core_views.store, name='store'),
]
