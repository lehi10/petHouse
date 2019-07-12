from django.db import models
from apps.proveedor.models import Producto

class Oferta(models.Model):
    id_oferta = models.AutoField(primary_key=True)
    nombre_oferta = models.CharField(max_length=50)
    descripcion_oferta = models.CharField(max_length=300)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
class Notificacion(models.Model):
	id_notificacion = models.AutoField(primary_key=True)
	id_usuario = models.CharField(max_length=5)
	mensaje = models.CharField(max_length=80)
	id_multiple = models.CharField(max_length=5)
	permisos_notificacion = models.CharField(max_length=20,blank=True,null=True)
	user_destino = models.CharField(max_length=20,null=True,blank=True)
	tiempo= models.DateField(blank=True,null=True)

