from django.shortcuts import render, redirect
from AppBlog.models import Autor, Categoria, Articulo
from AppBlog.forms import AutorFormulario, CategoriaFormulario, ArticuloFormulario
from django.db.models import Q

# Create your views here.
def homepage(request):
    articulos = Articulo.objects.all()
    
    if request.GET.get("busqueda"):
        busqueda = request.GET.get("busqueda")
        if busqueda:
            articulos = Articulo.objects.filter(Q(titulo__icontains=busqueda) | Q(autor__nombre__icontains=busqueda) | Q(categoria__nombre__icontains=busqueda))
    

    
    return render(request, 'inicio.html', {'articulos': articulos})

def autores(request):
    autores = Autor.objects.all()
    
    if request.method == 'POST':
        
        miFormulario = AutorFormulario(request.POST)
        
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            autor = Autor(nombre=datos['nombre'], email=datos['email'])
            autor.save()
            return redirect('Autores')
        
    else:
        
        miFormulario = AutorFormulario()
    
    return render(request, 'autores.html', {'miFormulario': miFormulario, 'autores': autores})

def categorias(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        
        miFormulario = CategoriaFormulario(request.POST)
        
        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            categoria = Categoria(nombre=datos['nombre'])
            categoria.save()
            return redirect('Categorias')
    else:
        
        miFormulario = CategoriaFormulario()
        
    return render(request, 'categorias.html', {'miFormulario': miFormulario, 'categorias': categorias})

def articulos(request):
    articulos = Articulo.objects.all()
    
    if request.method == 'POST':
        
        miFormulario = ArticuloFormulario(request.POST)

        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            articulo = Articulo(categoria=datos['categoria'], autor=datos['autor'], titulo=datos['titulo'], texto=datos['texto'], fecha_publicacion=datos['fecha_publicacion'])
            articulo.save()
            return redirect('Articulos')
    
    else:
        miFormulario = ArticuloFormulario()
    
    return render(request, 'articulos.html', {'miFormulario': miFormulario, 'articulos': articulos})