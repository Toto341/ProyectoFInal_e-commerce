from django.db import models
from django.contrib.auth.models import User

class ProductosCategorias(models.Model):

    # Los productos van a estar organizados por categorias: hombres, niños, damas, etc
    
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=45)  

    def __str__(self):
        return f"{self.categoria}" 


class ProductosMarcas(models.Model):

    # Cada producto tiene su correspondiente marca

    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=45)    

    def __str__(self):
        return f" {self.marca}"

class Productos(models.Model):
    
    # Este modelo va a almacenar los datos de todos los productos, en este caso calzados

    id_producto = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(ProductosCategorias, on_delete=models.CASCADE)
    marca = models.ForeignKey(ProductosMarcas, on_delete=models.CASCADE)
    precio = models.FloatField()
    titulo = models.CharField(max_length=60)    
    descripcion_corta = models.CharField(max_length=60)    
    descripcion_amplia = models.TextField(max_length=500)    
    id_usuario = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)     
    foto = models.ImageField(upload_to='fotos_productos/', blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)



class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
