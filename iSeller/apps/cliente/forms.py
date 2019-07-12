from django import forms

from apps.registro.models import Persona
from apps.cliente.models import Pedidos


class CrearPedidoForm(forms.ModelForm):
	class Meta:
		model = Pedidos
		fields = [
				#'idCliente',
				'nombre',
				'categoria',
				'descripcion',
				#'fecha_pedido',
		]
		labels = {
				'nombe': '¿ Qué esta buscando ?',
				'categoria':'Eliga una categoría',
				'descripcion': 'De una descripción',
		}
		categoriasList = (
			('veterinaria', 'Veterinaria'),
			('tienda', 'Tienda para Mascotas'),
			('spa', 'Spa para Mascotas'),
		)
		
		widgets ={
				'nombre':forms.TextInput(attrs={'class':'form-control'}),
				'categoria':forms.Select(attrs={'class': 'form-control'}, choices=( (x ) for x in categoriasList ),),
				'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
		}

