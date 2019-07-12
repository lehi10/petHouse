from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.core.exceptions import ObjectdoesNotExist
# Create your views here.
from apps.registro.forms import RegistroForm, RegistroUsuarioForm , RegistroProveedorForm, RegistroUsuarioProveedorForm
from apps.registro.forms import LoginForm


from apps.cliente.views import index, perfilCliente

from django.views.generic import ListView , CreateView
from apps.registro.models import Persona, UsuariosTabla
from apps.cliente.models import Cliente
from apps.intermediario.models import Intermediario 

"""
    Función para iniciar sesión
"""
def iniciarSesion( request, user):
    request.session['usuario'] = user.values()[0]['usuario']
    request.session['correo'] = user.values()[0]['email']
    request.session['id_user'] = user.values()[0]['id']
    request.session['permisos'] = user.values()[0]['permisos']
    request.session['isLogin']=True
    
def permisosUsuario(request):
    return request.session['permisos']

"""
    Funcion para cerrar Sesión
"""
def cerrarSesion(request ): 
    del request.session['id_user']
    del request.session['permisos']
    del request.session['usuario']
    del request.session['correo']
    request.session['isLogin']=False

""""
    Permite el logeo por nombre de usuario o correo
"""
def login_corre_or_username(nameus, clave):
    user = UsuariosTabla.objects.filter(usuario=nameus,password=clave)
    if user.exists():  
        return user
    else:
        user = UsuariosTabla.objects.filter(email=nameus,password=clave)
        return user

"""
    Vista de Registro Intermediario y Cliente
"""
def registro_view(request):
    error = request.GET.get('err',False)
    if request.method == 'POST':
        form_usuario =RegistroUsuarioForm(request.POST or None)
        form_persona = RegistroForm(request.POST or None)
        if form_usuario.is_valid() and form_persona.is_valid():            
                        
            datosUsuario = form_usuario.save(commit=False)
            datosUsuario.save()

            datosPersona = form_persona.save(commit=False)
            datosPersona.idUsuario_id  = datosUsuario.id
            datosPersona.save()

            
            if datosUsuario.permisos == 'cliente':
                #Registro en la tabla Cliente , para Clientes
                idPersona=Persona.objects.filter(idUsuario_id=datosUsuario.id)[0].idPersona
                TablaCliente = Cliente(persona_id=idPersona)
                TablaCliente.save()
            
            if datosUsuario.permisos == 'intermediario':
                #Registro en la tabla Intermediario , para Intermediarios
                idPersona=Persona.objects.filter(idUsuario_id=datosUsuario.id)[0].idPersona
                TablaIntermediario = Intermediario(idPersona_id=idPersona,calificacion=0)
                TablaIntermediario.save()

            name_us= form_usuario.cleaned_data.get("usuario")
            user = UsuariosTabla.objects.filter(usuario=name_us)           
            iniciarSesion(request,user)                     ## INICIAR SESSIÓN
            return redirect('/')
    else:
        form_persona = RegistroForm()
        form_usuario =RegistroUsuarioForm()
    return render(request,'registro/index.html', {'form':form_persona , 'form_usuario' : form_usuario,'error' : error} )
    
"""
    Vista de Registro Proveedor
"""
def registro_viewProveedor(request):
    error = request.GET.get('err',False)
    if request.method == 'POST':
        
        form_usuario = RegistroUsuarioProveedorForm(request.POST or None)
        form_proveedor = RegistroProveedorForm(request.POST or None)      
        if form_usuario.is_valid() and form_proveedor.is_valid():            
            
            datosUsuario = form_usuario.save(commit=False)
            datosUsuario.permisos='proveedor'
            datosUsuario.save()
            datosProveedor = form_proveedor.save(commit=False)
            datosProveedor.idUsuario_id  = datosUsuario.id
            datosProveedor.save()
            ## INICIAR SESSIÓN DESPUES DE REGISTRAR
            name_us= form_usuario.cleaned_data.get("usuario")
            user = UsuariosTabla.objects.filter(usuario=name_us)           
            iniciarSesion(request,user)             
            return redirect('/')
    else:
        form_proveedor = RegistroProveedorForm()
        form_usuario =RegistroUsuarioProveedorForm()    
    return render(request,'registro/regProveedor.html', {'form_proveedor':form_proveedor , 'form_usuario' : form_usuario,'error' : error} )
    
"""
    Función login, que recibe por POST los parametros de usuario y contraseña
"""
def login_view(request):
    if request.method == 'POST':
        form_login=LoginForm(request.POST or None)
        if form_login.is_valid():
            name_us = form_login.cleaned_data.get("username")
            password_us = form_login.cleaned_data.get("password")
            user = login_corre_or_username(name_us,password_us)
            permisos = 'cliente'
            if user.exists():    
                iniciarSesion(request,user)                  ## INICIAR SESION
                return redirect('/')        
    form_login = LoginForm()
    return redirect('/registro?err=log')
    
"""
    Vista cerrar sesión 
"""
def logout_view(request):
    if request.session['isLogin'] == True:
        cerrarSesion(request)                                ## CERRAR SESION
    return redirect('/')
