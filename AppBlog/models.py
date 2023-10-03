from django.db import models

# Create your models here.
class Autor(models.Model):    
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    categoria = models.ForeignKey(Categoria, blank=True, on_delete=models.CASCADE, null=True)
    autor = models.ForeignKey(Autor, blank=True, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=250)
    fecha_publicacion = models.DateTimeField()

    