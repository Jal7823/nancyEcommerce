from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from import_export import resources
from django.views.generic import DeleteView, DetailView, ListView, UpdateView,CreateView
from django.shortcuts import render,redirect
from productos.models import *
from usuarios.models import Usuario
from .forms import CrearProducto,CrearUsuario
from datetime import datetime
from usuarios.forms import crearUsuariosPanel,CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def panel(request):
    clientes = Usuario.objects.filter(
        Q(usuario_administrador=False )&
        Q(staff=False)
        ).count()

    usuarios = Usuario.objects.filter(
        Q(usuario_administrador=False )
        ).count()

    productos = Producto.objects.all().count()
    productosWidget = Producto.objects.all()[:5]
    # stockWidget = Producto.objects.filter(stock__gt=1)
    stockWidget = Producto.objects.filter(stock__gt=1)[:5]
    context = {
        'title':'Panel principal',
        'clientes': clientes,
        'productos':productos,
        'usuarios':usuarios,
        'productosWidget':productosWidget,
        'stockWidget':stockWidget,

    }
    return render(request, 'panel/panelBase.html',context)
# PRODUCTOS CRUD
def panelProductos(request):


    productos = Producto.objects.all()

    context = {
        'title':'panel productos',
        'productos': productos,
    }
    return render(request, 'panel/productos/productosPanel.html', context)

class crearProductos(SuccessMessageMixin,CreateView):
    model = Producto
    form_class = CrearProducto
    template_name = 'panel/productos/crearProductos.html'
    success_url = reverse_lazy('panelProductos')
    class Meta:
       labels = {
         'caracteristica':'Tallas'
    }

    def get_context_data(self, **kwargs):
        context = super(crearProductos, self).get_context_data(**kwargs)
        context['title']='Crear Productos'
        return context

class crearCaracteristica(SuccessMessageMixin,CreateView):
    model = Caracteristica
    fields ='__all__'
    template_name = 'panel/productos/crearProductos.html'

    success_url = reverse_lazy('crearCaracteristica')

    
    def get_context_data(self, **kwargs):
        context = super(crearCaracteristica, self).get_context_data(**kwargs)
        context['messages'] = messages.info(self.request,'Creacion exitosa')
        context['title'] = 'crear caracteristica'
        return context
    
class crearGenero(SuccessMessageMixin,CreateView):
    model = Genero
    fields ='__all__'
    template_name = 'panel/productos/crearProductos.html'
    success_messages = "Genero creado con exito"
    success_url = reverse_lazy('crearGenero')

    
    def get_context_data(self, **kwargs):
        context = super(crearGenero, self).get_context_data(**kwargs)
        context['messages'] = messages.info(self.request,'Creacion exitosa')
        context['title'] = 'crear genero'
        return context
    
class crearMarca(SuccessMessageMixin,CreateView):
    model = Marca
    fields ='__all__'
    template_name = 'panel/productos/crearProductos.html'
    success_url = reverse_lazy('crearMarca')

    
    def get_context_data(self, **kwargs):
        context = super(crearMarca, self).get_context_data(**kwargs)
        context['messages'] = messages.info(self.request,'Creacion exitosa')
        context['title'] = 'crear marca'
        return context

class crearColores(SuccessMessageMixin,CreateView):
    model = Color
    fields ='__all__'
    template_name = 'panel/productos/crearProductos.html'
    success_url = reverse_lazy('crearColores')

    
    def get_context_data(self, **kwargs):
        context = super(crearColores, self).get_context_data(**kwargs)
        context['messages'] = messages.info(self.request,'Creacion exitosa')
        context['title'] = 'crear marca'
        return context
    
class actualizarProducto(SuccessMessageMixin,UpdateView):
    model = Producto
    form_class = CrearProducto
    template_name  = 'panel/productos/actualizarProducto.html'  
 
    success_url=reverse_lazy('panelProductos')

    def get_context_data(self, **kwargs):
        context = super(actualizarProducto, self).get_context_data(**kwargs)
        context['title']='Actualizar Productos'
        return context

class detalleProducto(DetailView):
    model = Producto
    template_name  = 'panel/productos/detalleProducto.html'   
    success_url=reverse_lazy('panelProductos')

    
    def get_context_data(self, **kwargs):
        context = super(detalleProducto, self).get_context_data(**kwargs)
        context['title'] = 'detalle del producto'
        return context

class eliminarProducto(SuccessMessageMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('panelProductos')



 
# PRODUCTOS USUARIOS
def panelUsuarios(request):
    usuarios = Usuario.objects.filter(
        Q(staff=True) |
        Q(usuario_administrador=True) 
    )

    context = {
        'title':'panel usuarios',
        'usuarios': usuarios,
    }
    return render(request, 'panel/usuarios/usuariosPanel.html', context)

def crearUsuarios(request):
    data = {
        'form': crearUsuariosPanel(),
        'title':'crear usuario'
    }

    if request.method == 'POST':
        formulario = crearUsuariosPanel(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            return redirect(to='panelUsuarios')

        data['form'] = formulario
        messages.error(request, 'algo fallo en la suscripcion')
    return render(request, 'panel/usuarios/crearUsuario.html', data)

class eliminarUsuario(SuccessMessageMixin,DeleteView):
    model = Usuario
    success_url = reverse_lazy('panelUsuarios')

class actualizarUsuario(UpdateView):
    model = Usuario
    form_class = CrearUsuario
    template_name  = 'panel/usuarios/actualizarUsuario.html'   
    success_url=reverse_lazy('panelUsuarios')

    def get_context_data(self, **kwargs):
        context = super(actualizarUsuario, self).get_context_data(**kwargs)
        context['title']='Actualizar Usuario'

        return context

class detalleUsuario(DetailView):
    model = Usuario
    template_name  = 'panel/usuarios/detalleUsuario.html'   
    success_url=reverse_lazy('panelUsuarios')

    
    def get_context_data(self, **kwargs):
        context = super(detalleUsuario, self).get_context_data(**kwargs)
        context['title']='Crear Usuario'

        return context
    

# PRODUCTOS CLIENTES
def panelClientes(request):
    clientes = Usuario.objects.filter(
        Q(usuario_administrador=False)
    )

    

    context = {
        'title':'panel clientes',
        'clientes': clientes
    }
    return render(request, 'panel/clientes/clientesPanel.html', context)

def crearCliente(request):
    data = {
        'form': CustomUserCreationForm(),
        'title':'crear cliente'
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            messages.info(request,'Cliente creado con exito')
            return redirect(to='panelUsuarios')

        data['form'] = formulario
        messages.error(request, 'algo fallo en la suscripcion')
    return render(request, 'panel/usuarios/crearUsuario.html', data)
    
    
    def get_context_data(self, **kwargs):
        context = super(crearCliente, self).get_context_data(**kwargs)
        context['title']='Crear Clientes'
        return context

class actualizarCliente(SuccessMessageMixin,UpdateView):
    model = Usuario
    form_class = CrearUsuario
    template_name  = 'panel/clientes/actualizarCliente.html'   
    success_url=reverse_lazy('panelClientes')

    def get_context_data(self, **kwargs):
        context = super(actualizarCliente, self).get_context_data(**kwargs)
        context['title']='Actualizar Clientes'
        return context

class detalleCliente(DetailView):
    model = Usuario
    template_name  = 'panel/clientes/detalleCliente.html'   
    success_url=reverse_lazy('usuariosClientes')

    
    def get_context_data(self, **kwargs):
        context = super(detalleCliente, self).get_context_data(**kwargs)
        context['title']='Crear Clientes'

        return context
    model = Usuario
    template_name = "panel/clientes/detalleCliente.html"
    
    def get_context_data(self, **kwargs):
        context = super(detalleCliente, self).get_context_data(**kwargs)
        context['title']='Detalle del cliente'
        return context
    
class eliminarCliente(DeleteView):
    model = Usuario
    success_url = reverse_lazy('panelClientes')

