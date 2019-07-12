from django.conf.urls import url, include
from apps.cliente.views import index,pagos, perfilCliente, carritoCliente, editarInformacion_view,listaDeseos,editarPedido,eliminarPedido,crearPedido, mostrarPedidos,eliminarFavorito 


urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilCliente,name='perfil'),
    url(r'^carrito$',carritoCliente,name='carrito'),
    url(r'^pedidos$',mostrarPedidos, name='pedidos'),
    url(r'^crearPedido$',crearPedido, name='crearPedido'),
    url(r'^editarInf/(?P<id_user>.*)$',editarInformacion_view, name='editarInf'),
    url(r'^editarPed/(?P<idp>.*)$',editarPedido, name='editarPed'),
    url(r'^deseos$',listaDeseos, name='deseos'),
    url(r'^pagos$',pagos, name='pagos'),
    url(r'^deleteP/(?P<idp>.*)$',eliminarPedido, name='deleteP'),
    url(r'^deleteFav/(?P<idf>.*)$',eliminarFavorito, name='deleteFav'), 


]