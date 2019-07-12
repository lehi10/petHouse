from django.shortcuts import render
from django.shortcuts import redirect
from apps.tienda.views import error404


from django.http import HttpResponse
from apps.registro.models import Persona
from apps.cliente.models import Pedidos
from apps.proveedor.models import Categoria
from django.http import JsonResponse
from apps.intermediario.models import Respuesta
from apps.dashboard.models import Notificacion
# Create your views here.
def respuesta(request):
	mensaje=request.GET.get('mensaje',None)
	mi_pedido=request.GET.get('id_pedido',None)
	data ={
		'is_taken': Categoria.objects.all().exists()
	}
	todo_pedido=Pedidos.objects.filter(idPedido=mi_pedido)
	nueva_respuesta = Respuesta(respuesta=mensaje,idPedido_id=mi_pedido)
	nueva_respuesta.save()
	mi_mensaje="El usuario "+ str(request.session.get('id_user')) + "a respondido tu pedido"
	mi_notificacion= Notificacion(id_usuario=request.session.get('id_user'),mensaje=mi_mensaje,id_multiple=mi_pedido,user_destino=todo_pedido[0].idCliente_id)
	mi_notificacion.save()
	print("--------//////------->",mi_pedido)
	return JsonResponse(data)
	
def index(request):
	if 'isLogin' not in request.session or request.session.get('permisos')!='intermediario':
		return redirect('/')

	categoria=''
	if  'categoria' in request.GET and request.GET['categoria'] != "" :	
		categoria= request.GET['categoria']
		pedidos = Pedidos.objects.filter(categoria__icontains = categoria ) 
	
	else:
		pedidos = Pedidos.objects.select_related() 
		
	categorias=Categoria.objects.all()
	contexto={'mis_categorias': categorias,'mis_pedidos':pedidos}
	return render(request, 'intermediario/index.html',contexto)


def perfilIntermediario(request):
    ## VALIDACION PARA SABER SI EL USUARIO HA SIDO LOGEADO Y SI TIENE PERMISOS PARA ACCEDER
	if request.session.get('isLogin') != True and request.session.get('permisos') != 'intermediario':
		return error404(request);
	idUsuario = request.session.get('id_user')
	usuario = Persona.objects.filter(idUsuario=idUsuario)
	contexto= {'mi_usuario':usuario , 'id_user':idUsuario}
	return render(request,'intermediario/perfil.html',contexto)     

