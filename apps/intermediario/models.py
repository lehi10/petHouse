from django.db import models
from apps.registro.models import Persona
from apps.cliente.models import Pedidos

class Intermediario(models.Model):
    idIntermediario = models.AutoField(primary_key=True, null=False,blank=False)
    idPersona = models.OneToOneField(Persona,null=False,blank=False, on_delete=models.CASCADE)
    calificacion = models.IntegerField(default=0)
class Respuesta(models.Model):
	idRespuesta = models.AutoField(primary_key=True, null=False,blank=False)
	respuesta = models.CharField(max_length=200)
	idPedido = models.ForeignKey(Pedidos,null=False,blank=False,on_delete=models.CASCADE)

    
