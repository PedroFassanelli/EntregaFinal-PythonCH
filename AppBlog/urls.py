from django.urls import path, include
from . import views

urlpatterns = [
    
    path('autores', views.autores, name="Autores"),
    path('categorias', views.categorias, name="Categorias"),
    path('articulos', views.articulos, name="Articulos"),
]