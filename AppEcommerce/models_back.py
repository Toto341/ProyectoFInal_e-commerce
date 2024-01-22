from django.db import models
from django.contrib.auth.models import User

class ProductosCategorias(models.Model):

    # Los productos van a estar organizados por categorias: hombres, niños, damas, etc
    
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=45)  

    def __str__(self):
        return f"Id:  {self.id_categoria} - Categoría: {self.categoria}" 


class ProductosMarcas(models.Model):

    # Cada producto tiene su correspondiente marca

    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=45)    

    def __str__(self):
        return f"Id:  {self.id_marca} - Marca: {self.marca}"


class ProductosImagenes(models.Model):

    # Cada producto puede tener cero a n imágenes por eso se usa un modelo aparte

    id_producto_imagen = models.AutoField(primary_key=True)
    id_producto = models.IntegerField()
    imagen = models.CharField(max_length=45)    
    orden = models.IntegerField()

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

class ProductosImagenes(models.Model):

    # Cada producto puede tener cero a n imágenes por eso se usa un modelo aparte

    id_producto_imagen = models.AutoField(primary_key=True)
    id_producto = models.IntegerField()
    imagen = models.CharField(max_length=45)    
    orden = models.IntegerField()

class ProductosEvaluaciones(models.Model):

    # Los usuarios pueden hacer evaluaciones sobre los productos comprados, pero el comentario debe ser aprobado por el admin, también lo pueden calificar de 1 a 5

    id_producto_comentario = models.AutoField(primary_key=True)
    id_producto = models.IntegerField()
    comentario = models.CharField(max_length=255)   
    calificacion = models.IntegerField()
    id_usuario = models.IntegerField()
    fecha_publicacion = models.DateField(null=False)

class ProductosEvaluacionesEstados(models.Model):    

    # Las evaluaciones pueden estar, pendientes = 0 (por defecto), aprobada = 1 (visible para visitantes del sitio), rechazada = 2 (no se ve)
    
    id_estado = models.AutoField(primary_key=True)
    estado = models.IntegerField()    

class ProductosTalles(models.Model):    

    # Aqui se guardan todos los talles diponibles para los calzados

    id_talle = models.AutoField(primary_key=True)
    talle = models.IntegerField()    

    def __str__(self):
        return f"Id:  {self.id_talle} - Talle: {self.talle}"


class ProductosTallesDiponibles(models.Model):    

    # De un mismo producto, la empresa puede tener distinta cantidad en stock de cada talle, la finalidad de este modelo es reflejar esas variaciones

    id_talle_diponilbe = models.AutoField(primary_key=True)
    id_producto = models.IntegerField()    
    id_talle = models.IntegerField()    
    stock = models.IntegerField()    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
