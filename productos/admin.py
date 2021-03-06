from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import Producto,Marca,Caracteristica,ImagenProducto,Genero



class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ('id','imagen',)


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)
    search_fields = ('nombre',)
    list_editable = ('nombre',)


class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','parent',)
    search_fields = ('nombre','parent',)
    list_editable = ('nombre','parent',)


class ProductosResource(resources.ModelResource):
    class Meta:
        model = Producto
        exclude = ('id',)

class MarcaResource(resources.ModelResource):

    class Meta:
        model = Marca




class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','cod','nombre', 'imagen','precio','marca' ,'stock',)
    list_filter  = ( 'marca', 'stock',)
    search_fields = ('cod','nombre', 'marca', 'precio')
    list_editable = ('cod','nombre','marca', 'precio','stock','imagen',)
    readonly_fields = ('created', 'updated')
    resources_class = ProductosResource


class MarcaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','categoria')
    search_fields = ('categoria',)
    resources_class = MarcaResource


class OrderCantidadAdmin(admin.ModelAdmin):
    list_display = ('producto','cantidad',)
    list_filter = ('producto','cantidad',)


admin.site.register(Caracteristica,CaracteristicaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(ImagenProducto, ImagenProductoAdmin)
admin.site.register(Genero, GeneroAdmin)
