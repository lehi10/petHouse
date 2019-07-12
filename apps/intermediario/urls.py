from django.conf.urls import url, include
from apps.intermediario.views import index
from apps.intermediario.views import perfilIntermediario
from apps.intermediario.views import respuesta
urlpatterns =[ 
    url(r'^$',index, name='index'),
    url(r'^perfil$',perfilIntermediario,name='perfil'),
    url(r'^responder_p$',respuesta,name='respuesta_pend'),

]