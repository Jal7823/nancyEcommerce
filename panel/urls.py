from django.urls import path, include
from .views import *

urlpatterns = [
    path('', panel, name='panel'),
    # productos
    path('panelProductos/', panelProductos, name='panelProductos'),
    path('crearProductos/', crearProductos.as_view(), name='crearProductos'),
    path('crearCaracteristica/', crearCaracteristica.as_view(), name='crearCaracteristica'),
    path('crearGenero/', crearGenero.as_view(), name='crearGenero'),
    path('crearMarca/', crearMarca.as_view(), name='crearMarca'),
    path('crearColores/', crearColores.as_view(), name='crearColores'),
    path('actualizarProducto/<int:pk>', actualizarProducto.as_view(), name='actualizarProducto'),
    path('detalleProducto/<int:pk>', detalleProducto.as_view(), name='detalleProducto'),
    path('eliminarProducto/<int:pk>', eliminarProducto.as_view(), name='eliminarProducto'),
    # usuarios
    path('panelUsuarios/', panelUsuarios, name='panelUsuarios'),
    path('crearUsuarios/', crearUsuarios, name='crearUsuarios'),
    path('actualizarUsuario/<int:pk>', actualizarUsuario.as_view(), name='actualizarUsuario'),
    path('detalleUsuario/<int:pk>', detalleUsuario.as_view(), name='detalleUsuario'),
    path('eliminarUsuario/<int:pk>', eliminarUsuario.as_view(), name='eliminarUsuario'),

    # clientes
    path('panelClientes/', panelClientes, name='panelClientes'),
    path('crearCliente/', crearCliente, name='crearCliente'),
    path('actualizarCliente/<int:pk>', actualizarCliente.as_view(), name='actualizarCliente'),
    path('detalleCliente/<int:pk>', detalleCliente.as_view(), name='detalleCliente'),
    path('eliminarCliente/<int:pk>', eliminarCliente.as_view(), name='eliminarCliente'),


]
