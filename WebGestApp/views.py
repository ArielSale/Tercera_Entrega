from django.shortcuts import render, redirect
from .models import Cliente, Proveedor, Producto
from .forms import ClienteForm, ProveedorForm, ProductoForm 
from .forms import BuscaClienteForm, BuscaProveedorForm
from django.shortcuts import get_object_or_404


def inicio(request):
    return render(request, "WebGestApp/index.html")

def clientes(request):
    return render(request, "WebGestApp/clientes.html")

def proveedores(request):
    return render(request, "WebGestApp/proveedores.html")

def stock(request):
    return render(request, "WebGestApp/stock.html")

def contact_me(request):
    return render(request, "WebGestApp/contact_me.html")

def about(request):
    return render(request, "WebGestApp/about.html")

def alta_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "WebGestApp/clientes.html")
    context = {'form': form}
    return render(request, "WebGestApp/clientes/alta_cliente.html", context)

def alta_proveedor(request):
    form = ProveedorForm()
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "WebGestApp/proveedores.html")
    context = {'form': form}
    return render(request, "WebGestApp/proveedores/alta_proveedor.html", context)

def alta_producto(request):
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "WebGestApp/stock.html")
    context = {'form': form}
    return render(request, "WebGestApp/stock/alta_producto.html", context)

def listar_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'WebGestApp/clientes/listar_clientes.html', context)

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {'proveedores': proveedores}
    return render(request, 'WebGestApp/proveedores/listar_proveedores.html', context)

def listar_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'WebGestApp/stock/listar_productos.html', context)

def buscar_cliente(request):
    form = BuscaClienteForm()
    clientes = []

    if request.method == 'POST':
        form = BuscaClienteForm(request.POST)
        if form.is_valid():
            cuit = form.cleaned_data['cuit']
            clientes = Cliente.objects.filter(cuit__contains=cuit)

    context = {'form': form, 'clientes': clientes}
    return render(request, 'WebGestApp/clientes/buscar_cliente.html', context)

def buscar_proveedor(request):
    form = BuscaProveedorForm()
    proveedores = []

    if request.method == 'POST':
        form = BuscaProveedorForm(request.POST)
        if form.is_valid():
            cuit = form.cleaned_data['cuit']
            proveedores = Proveedor.objects.filter(cuit__contains=cuit)

    context = {'form': form, 'proveedores': proveedores}
    return render(request, 'WebGestApp/proveedores/buscar_proveedor.html', context)

def detalle_cliente(request, cliente_cuit):
    cliente = get_object_or_404(Cliente, cuit=cliente_cuit)
    return render(request, 'WebGestApp/clientes/detalle_cliente.html', {'cliente': cliente})

def detalle_proveedor(request, proveedor_cuit):
    proveedor = get_object_or_404(Proveedor, cuit=proveedor_cuit)
    return render(request, 'WebGestApp/proveedores/detalle_proveedor.html', {'proveedor': proveedor})

