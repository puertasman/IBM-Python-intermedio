from . import views as pages_views
from django.urls import path

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', pages_views.page, name='page')
]
