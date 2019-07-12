from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from apps.dashboard.models import Oferta
from apps.proveedor.models import Producto
from apps.proveedor.models import Categoria
from apps.intermediario.views import index as index_intermediario
from apps.proveedor.views import index as index_proveedor
from apps.cliente.views import index as index_cliente
from apps.cliente.models import Lista_deseos , Cliente
from apps.registro.models import Persona
from apps.dashboard.models import Notificacion
from apps.cliente.models import Pedidos
from django.http import JsonResponse
def insertar_notificacion(request):
	print("im heeeere")
	el_mensaje = request.GET.get('mensaje', None)
	id_usuarioG=request.session['id_user']
	print("--------------------->",el_mensaje)
	
	if(request.session['permisos']=="cliente"):
		new_pe=Pedidos.objects.all().order_by("-idPedido")[0]
		print("El Max:->",new_pe.idPedido)
		nueva_notificacion = Notificacion(id_usuario=id_usuarioG,mensaje=el_mensaje,id_multiple=new_pe.idPedido,permisos_notificacion="intermediario")
		nueva_notificacion.save()
	data={
		'is_taken': Notificacion.objects.filter(id_usuario=id_usuarioG).exists()
	}
	return JsonResponse(data)
def notificaciones(request):
	print("======Notificaciones======")
	print(request.session['id_user'])
	id_usuarioG=request.session['id_user']
	if(request.session['permisos']=="cliente"):
		noti = Notificacion.objects.filter(user_destino=id_usuarioG)
	if(request.session['permisos']=="intermediario"):
		print("debi entrar aqui: ")
		noti = Notificacion.objects.filter(permisos_notificacion="intermediario")
	for x in noti:
		print("looooooooooook: ",x.mensaje)
	return render(request,'base/notificaciones.html',{'notifi':noti})

def index2(request):
    return render(request,'index.html')


def tienda(request):
    return render(request,'tienda/index.html')

def contenido_view(request):
	if 'isLogin' in request.session  and request.session['isLogin']:
		idUsuario = request.session['permisos']
		if(idUsuario=="intermediario"):
			return index_intermediario(request)
		if(idUsuario=='proveedor'):
			return index_proveedor(request)
		if(idUsuario=='cliente'):
				return index_cliente(request)	
	else:
		keywords=''
		categoria=''
		if 'categoria' in request.GET and  request.GET['categoria'] != "" :	
			categoria= request.GET['categoria']
			ofertas = Producto.objects.filter(categoria__icontains = categoria ) ## CAMBIAR DE PRODUCTOS A OFERTAS Y PROMOCIONES
		
		else:
			if 'query' in request.GET and  request.GET['query'] != "" :	
				keywords= request.GET['query']
				ofertas = Producto.objects.filter(nombre__icontains = keywords ) ## CAMBIAR DE PRODUCTOS A OFERTAS Y PROMOCIONES
			else:
				ofertas = Producto.objects.select_related() ## CAMBIAR DE PRODUCTOS A OFERTAS Y PROMOCIONES
			
		categorias=Categoria.objects.all()
		contexto={'mis_categorias': categorias, 'ofert_list' : ofertas}
		return render(request,'index.html',contexto)

def detallesItem(request):
	if 'id' not in request.GET:
		return redirect('/')
	
	
	idProducto= request.GET['id']
	item =Producto.objects.filter(idProducto=idProducto).all()
	
	

	if len(item) != 1:
		return redirect('/')
	
	
	statusDeseo=False	
	if 'ald' in request.GET and request.GET['ald']=='1': 
		if 'isLogin' in request.session and request.session.get('permisos') =='cliente':
			idUsuario = request.session.get('id_user')
			idPersona =  Persona.objects.filter(idUsuario=idUsuario).all()[0].idPersona
			cliente= Cliente.objects.filter(persona=idPersona).all()[0]

			itemLista = Lista_deseos(idCliente=cliente, idProducto=item[0])
			itemLista.save()	
			statusDeseo=True
		else:
			return redirect('/registro')
	item_set={'detalles' : item,'id':idProducto,'estadoListaDeseos':statusDeseo}
	
	return render(request,'tienda/item.html',item_set)