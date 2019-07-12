from django.conf.urls import url, include
from apps.proveedor.views import index, perfilProveedor, registroProducto_view,misproductos,MostrarRequerimientos

urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilProveedor,name='perfil'),
    url(r'^requerimientos$',MostrarRequerimientos,name='requeridos'),
    url(r'^misproductos$',misproductos,name='m_productos'),
    url(r'^regProducto$',registroProducto_view,name='Registrar Producto'),
    
]