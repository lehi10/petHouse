from django import forms
from apps.proveedor.models import Producto



class RegistroProductosForm(forms.ModelForm):
      class Meta:
            model = Producto
            fields =[
            'nombre',
            'medidas',
            'marca',
            'stock',
            'tags',
            'categoria',
            'info',
            'precioBasico',
            'descripcion',
            'urlImagen',
		]
            labels = {
		'nombre':       'Nombre del Producto',
            'medidas':      'Medidas y/o Dimensiones',
            'marca':        'Marca',
            'stock':        'Stock actual',
            'tags':         'Tags',
            'categoria':    'Categoria',
            'info':         'Información',
            'precioBasico': 'Precio Base',
            'descripcion':  'Descripción adicional',
            'urlImagen': 'Seleccione una Imagen',
		}

            
            categoriasList = (
                  ('veterinaria', 'Veterinaria'),
                   ('tienda', 'Tienda para Mascotas'),
                  ('spa', 'Spa para Mascotas'),
            )

            widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'medidas':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'stock':forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'tags':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class': 'form-control'}, choices=( (x ) for x in categoriasList ),),
            'info':forms.Textarea(attrs={'class':'form-control','rows': 6, 'maxlength': 480}),
            'precioBasico':forms.TextInput(attrs={'class':'form-control' ,'type':'number', 'step':'0.01'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows': 6, 'maxlength': 480}),
		}
      def clean_nombre(self): 
            nombre = self.cleaned_data.get("nombre") 
            if not len(nombre)<=100: 
                  raise forms.ValidationError("El nombre no puede ser mas grande de 100 caracteres")  
            return nombre 

      def clean_medidas(self): 
            medidas = self.cleaned_data.get("medidas") 
            return medidas 
      
      def clean_marca(self): 
            marca = self.cleaned_data.get("marca") 
            if not len(marca) <=50: 
                  raise forms.ValidationError("Especifiquelo en menoes de 50 caracteres") 
            return marca 
      
      def clean_info(self): 
            info = self.cleaned_data.get("info") 
            if not len(info) <= 500: 
                  raise forms.ValidationError("Sea mas consiso especifiquelo en menoes de 500 caracteres") 
            return info 
      
      def clean_descripcion(self): 
            descripcion = self.cleaned_data.get("descripcion") 
            if not len(descripcion) <= 500: 
                  raise forms.ValidationError("Sea mas consiso especifiquelo en menoes de 500 caracteres") 
            return descripcion 
