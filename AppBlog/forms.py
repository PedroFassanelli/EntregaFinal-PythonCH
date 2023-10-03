from django import forms
from .models import Categoria, Autor, Articulo

class AutorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    
class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    
class ArticuloFormulario(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    autor = forms.ModelChoiceField(queryset=Autor.objects.all())
    titulo = forms.CharField(max_length=50)
    texto = forms.CharField(max_length=250)
    fecha_publicacion = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M:%S']
    )
