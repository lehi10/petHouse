from django import forms
from apps.registro.models import Persona, UsuariosTabla
from apps.proveedor.models import Proveedor
import time
from django.utils.translation import gettext as _
from django.core.validators import validate_email


class RegistroUsuarioForm(forms.ModelForm):
	class Meta:
		model = UsuariosTabla
		fields =[
			'usuario',
			'password',
			'permisos',
			'email',
		]
		labels = {
			'usuario' : 'Usuario',
			'password': 'Password',
			'permisos': '¿Como desea usar su cuenta ?',
			'email': 'Email',
		}
		permisosList = (
        ('cliente', 'Quiero hacer compras'),
        ('intermediario', 'Quiero ofrecer productos de terceros (Intermediario)'),
    	)
		widgets = {
			'usuario':forms.TextInput(attrs={'class':'form-control'}),
			'password':forms.TextInput(attrs={'class': 'form-control','type':'password'}),
			'permisos':forms.Select(attrs={'class': 'form-control'}, choices=( (x ) for x in permisosList ),),
			'email':forms.EmailInput(attrs={'class': 'form-control'}),
		}

	def clean_usuario(self):
		usuario = self.cleaned_data.get("usuario")
		if  UsuariosTabla.objects.filter(usuario=usuario).exists():
			raise forms.ValidationError("El nombre de usuario ya esta en uso")
		return usuario
	
	def clean_password(self):
		password = self.cleaned_data.get("password")
		if not len(password) >= 8:
			raise forms.ValidationError("La contraseña debe tener como mínimo 8 caracteres")
		return password

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveedor = email.split("@")
		if -1 != proveedor.find("."):
			dominio, extension = proveedor.split(".")
			if not extension == "com":
				raise forms.ValidationError("Utilize un email con la extension .com")
			if UsuariosTabla.objects.filter(email=email).exists():
				raise forms.ValidationError("Este correo ya esta siendo usado")
		else :
			raise forms.ValidationError("Utilize un email válido")
		#validate_email(email)
		return email

class RegistroForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = [
			'nombres',
			'apellidos',
			'sexo',
			'fecha_nac',
			'id_doc',
			'telf',
			'domicilio',
		]
		labels = {
			'nombres' :'Nombres',
			'apellidos': 'Apellidos',
			'sexo' : 'Sexo',
			'fecha_nac': 'Fecha de Nacimiento',
			'id_doc':'Documento de Identidad',
			'telf': 'Teléfono',
			'domicilio': 'Domicilio',	
		}

		generos = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    	)
		
		widgets = {
			'nombres':forms.TextInput(attrs={'class': 'form-control'}),
			'apellidos':forms.TextInput(attrs={'class': 'form-control'}),
			'sexo':forms.Select(attrs={'class': 'form-control'}, choices=( (x ) for x in generos ),),
			'fecha_nac':forms.DateInput(attrs={'class': 'form-control','type':'date'}),
			'id_doc':forms.TextInput(attrs={'class': 'form-control'}),
			'telf':forms.TextInput(attrs={'class': 'form-control'}),
			'domicilio':forms.TextInput(attrs={'class': 'form-control'}),
		}

	def save(self, commit=True):
		instance = super(RegistroForm, self).save(commit=False)
		self.Meta.model.idUsuario=0
		if commit:
			instance.save()
		return instance

	def clean_fecha_nac(self):
		fecha_nac = self.cleaned_data.get("fecha_nac")
		if not int(time.strftime("%Y")) - int(fecha_nac.year) >= 18:
			raise forms.ValidationError("Usted no cumple con el límite  mínimo de edad")
		return fecha_nac

	def clean_id_doc(self):
		id_doc = self.cleaned_data.get("id_doc")
		if not len(id_doc) == 8:
			raise forms.ValidationError("Su ID debe ser de 8 dígitos")
		if id_doc.isdigit() == False:
			raise forms.ValidationError("Su ID no es válido")
		return id_doc

	def clean_telf(self):
		telf = self.cleaned_data.get("telf")
		if len(telf) >= 6:
			if telf.isdigit() == False:
				raise forms.ValidationError("Ingrese un número válido")
		else: 
			raise forms.ValidationError("Ingrese un número válido")
		return telf


class RegistroProveedorForm(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = [
			'ruc',
			'razonSocial',
			'encargado',
			'categoria',
			'telf',
			'domicilio',
			'info',
		]
		labels = {
			'ruc' :'RUC',
			'razonSocial': 'Razón Social',
			'encargado' : 'Encargado',
			'categoria': 'Categoria',
			'telf':'Telefono de Contacto',
			'domicilio': 'Domicilio',
			'info': 'Información',	
		}
		
		categorias = (
        ('veterinaria', 'Veterinaria'),
        ('tienda', 'Tienda para Mascotas'),
		('spa', 'Spa para Mascotas'),
    	)
		
		widgets = {
			'ruc':forms.TextInput(attrs={'class': 'form-control'}),
			'razonSocial':forms.TextInput(attrs={'class': 'form-control'}),
			'encargado':forms.TextInput(attrs={'class': 'form-control'}),
			'categoria':forms.Select(attrs={'class': 'form-control'}, choices=( (x ) for x in categorias ),),
			'telf':forms.TextInput(attrs={'class': 'form-control'}),
			'domicilio':forms.TextInput(attrs={'class': 'form-control'}),
			'info':forms.Textarea(attrs={'class': 'form-control'}),			
		}

	def clean_ruc(self):
		id_doc = self.cleaned_data.get("ruc")
		if not len(id_doc) == 11:
			raise forms.ValidationError("Su RUC debe ser de 11 dígitos")
		if id_doc.isdigit() == False:
			raise forms.ValidationError("Su RUC no es válido")
		return id_doc

	def clean_telf(self):
		telf = self.cleaned_data.get("telf")
		if len(telf) >= 6:
			if telf.isdigit() == False:
				raise forms.ValidationError("Ingrese un número válido")
		else: 
			raise forms.ValidationError("Ingrese un número válido")
		return telf

class RegistroUsuarioProveedorForm(forms.ModelForm):
	class Meta:
		model = UsuariosTabla
		fields =[
			'usuario',
			'password',
			'email',
		]
		labels = {
			'usuario' : 'Usuario',
			'password': 'Password',
			'email': 'Email',
		}
		widgets = {
			'usuario':forms.TextInput(attrs={'class':'form-control'}),
			'password':forms.TextInput(attrs={'class': 'form-control','type':'password'}),
			'email':forms.EmailInput(attrs={'class': 'form-control'}),
		}

	def clean_usuario(self):
		usuario = self.cleaned_data.get("usuario")
		if  UsuariosTabla.objects.filter(usuario=usuario).exists():
			raise forms.ValidationError("El nombre de usuario ya esta en uso")
		return usuario
	
	def clean_password(self):
		password = self.cleaned_data.get("password")
		if not len(password) >= 8:
			raise forms.ValidationError("La contraseña debe tener como mínimo 8 caracteres")
		return password

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveedor = email.split("@")
		if -1 != proveedor.find("."):
			dominio, extension = proveedor.split(".")
			if not extension == "com":
				raise forms.ValidationError("Utilize un email con la extension .com")
			if UsuariosTabla.objects.filter(email=email).exists():
				raise forms.ValidationError("Este correo ya esta siendo usado")
		else :
			raise forms.ValidationError("Utilize un email válido")
		#validate_email(email)
		return email



class LoginForm(forms.Form):
	username = forms.CharField( widget=forms.TextInput,required=True)
	password = forms.CharField(	widget=forms.TextInput, required=True)
	"""def clean_username(self):
		username = self.cleaned_data.get("username")
		if Persona.objects.filter(usuario=username).exists():

		elif Persona.objects.filter(email=username).exists():"""


