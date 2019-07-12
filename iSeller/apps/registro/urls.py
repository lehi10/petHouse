from django.conf.urls import url, include

from apps.registro.views import  registro_view
from apps.registro.views import  login_view
from apps.registro.views import  logout_view , registro_viewProveedor

urlpatterns = [
		url(r'^$', registro_view, name="registroNuevo"),
        url(r'^Proveedor$', registro_viewProveedor, name="registroNuevoProovedor"),
        url(r'^login$', login_view),
        url(r'^logout$', logout_view),
        
]

 