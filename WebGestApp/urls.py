from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('stock/', views.stock, name='stock'),
    path('contact_me/', views.contact_me, name='contacto'),
    path('about/', views.about, name='about'),
    path('clientes/alta_cliente/', views.alta_cliente, name='alta_cliente'),
    path('proveedores/alta_proveedor/', views.alta_proveedor, name='alta_proveedor'),
    path('stock/alta_producto/', views.alta_producto, name='alta_producto'),
    path('clientes/listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('proveedores/listar_proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('stock/listar_productos/', views.listar_productos, name='listar_productos'),
    path('clientes/buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('proveedores/buscar_proveedor/', views.buscar_proveedor, name='buscar_proveedor'),
]