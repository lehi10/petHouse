from django.db import models
from apps.registro.models import UsuariosTabla


class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True, null=False,blank=False)
    idUsuario = models.OneToOneField(UsuariosTabla,null=False,blank=False, on_delete=models.CASCADE)
    ruc = models.CharField(db_index=True ,null=False,blank=False, max_length=20)
    razonSocial = models.CharField(db_index=True,null=False,blank=False, max_length=100)
    encargado = models.CharField(null=False,max_length=100)
    categoria = models.CharField(null=True,blank=False,max_length=20)
    telf = models.CharField(null=True,blank=False,max_length=15)
    domicilio = models.TextField(null=False, max_length=100)
    info = models.CharField(null=False,max_length=300)
    calificacion = models.IntegerField(default=0)

class Producto(models.Model):
    idProducto =models.AutoField(primary_key=True)
    idProveedor = models.ForeignKey(Proveedor,null=False,blank=False,on_delete=models.CASCADE)
    nombre = models.CharField(blank=True,max_length=100)
    medidas = models.CharField(blank=True,max_length=50)
    marca = models.CharField(default="",max_length=50)
    stock = models.IntegerField(default=0)
    calificacion = models.IntegerField(default=0)
    tags = models.CharField(default="",max_length=50)
    info =models.TextField(default="",max_length=500)
    precioBasico = models.FloatField(default=0)
    descripcion = models.TextField(default="",max_length=500)
    categoria = models.CharField(db_index=True,default="",max_length=100)
    urlImagen = models.ImageField(upload_to='productosImg')

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombre=models.CharField(blank=True,max_length=100)
class Requerimientos(models.Model):
    idRequerimiento= models.AutoField(primary_key=True)
    nombre=models.CharField(blank=True,max_length=100)
    descripcion=models.CharField(blank=True,max_length=300)
    cantidad=models.IntegerField(default=0)
    marca=models.CharField(blank=True,max_length=100)

