from . import views as blog_views
from django.urls import path

urlpatterns = [
    path('', blog_views.blog, name='blog'),
    path('category/<int:category_id>/', blog_views.category, name='category')
]
