from django.contrib import admin
from .models import Autor, Articulo, Categoria

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'email')
    list_display = ('nombre', 'email')


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'categoria', 'autor')
    list_display = ('titulo', 'categoria', 'autor', 'fecha_publicacion')
    

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre',)