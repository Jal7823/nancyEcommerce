from django import forms
from multiselectfield import MultiSelectField
from usuarios.models import Usuario
from productos.models import Producto,Caracteristica,Genero,Marca,Color




class CrearUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre','apellido','email','dni','imagen','tlf','loc','usuario_administrador')

class CrearProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cod','nombre','marca','colores','caracteristica','categoria','precio','descripcion','imagen','stock']
        widgets ={
            'caracteristica':forms.CheckboxSelectMultiple(),
            'colores':forms.CheckboxSelectMultiple(),
        }
        labels={
            'caracteristica':'Tallas',
            'Categoria':'Genero'
        }

class CrearCaracteristica(forms.ModelForm):
    class Meta:
        model = Caracteristica()
        fields = ['nombre',]
        widgets = {
            'nombre':forms.TextInput(attrs={'autofocus':True})
        }

class CrearGenero(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class CrearMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'


