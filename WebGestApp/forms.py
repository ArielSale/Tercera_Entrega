from django import forms
from .models import Cliente, Proveedor, Producto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['razon_social', 'cuit', 'email']
        labels = {
            'razon_social': 'Razon Social',
            'cuit': 'CUIT',
            'email': 'Email',
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['razon_social', 'cuit', 'email']
        labels = {
            'razon_social': 'Razon Social',
            'cuit': 'CUIT',
            'email': 'Email',
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']
        labels = {
            'nombre': 'Nombre del Producto',
            'precio': 'Precio de Venta',
            'stock': 'Stock',
        }

class BuscaClienteForm(forms.Form):
    cuit = forms.CharField()

class BuscaProveedorForm(forms.Form):
    cuit = forms.CharField()


#class BuscaClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cuit']
        labels = {'cuit': 'CUIT'}

#class BuscaProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['cuit']
        labels = {'cuit': 'CUIT'} 

