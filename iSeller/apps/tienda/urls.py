from django.conf.urls import url, include
from apps.tienda.views import index, error404,contacto

urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^404$',error404,name='error404'),
    url(r'^contacto$',contacto,name='contacto'),
]