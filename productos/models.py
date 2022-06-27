from django.db import models
from autoslug import AutoSlugField

class Caracteristica(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = 
    True, null=True)
    slug = AutoSlugField(populate_from='nombre', unique=True, null=False, editable=False)
    nombre = models.CharField(max_length=100,null=True,blank=True,verbose_name='nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.nombre]                  
        k = self.parent
        while k is not None:
            full_path.append(k.nombre)
            k = k.parent
        return ' : '.join(full_path[::-1])  

class Genero(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True,verbose_name='genero')

    def __str__(self):
        return self.nombre

class Marca(models.Model): 
    categoria = models.CharField(max_length=200, verbose_name='marca')
    imagen = models.ImageField(upload_to = 'prouctos',verbose_name='imagen',null=True,blank=True )

    def __str__(self):
        return self.categoria

class ImagenProducto(models.Model):
    imagen = models.ImageField(upload_to="products/%Y/%m/%d")
    def __str__(self):
        return str(self.id)

class Color(models.Model): 
    categoria = models.CharField(max_length=200, verbose_name='color')
    imagen = models.ImageField(upload_to = 'prouctos',verbose_name='imagen' ,blank=True, null=True)

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    cod = models.IntegerField(verbose_name='Codigo',null=True,blank=True)
    nombre = models.CharField(max_length=200, verbose_name='Producto')
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE, verbose_name='Marca')
    colores = models.ManyToManyField(Color,verbose_name='Colores',blank=True, null=True)
    caracteristica = models.ManyToManyField(Caracteristica,verbose_name='Tallas',blank=True, null=True)
    categoria = models.ForeignKey(Genero,on_delete=models.CASCADE, verbose_name='Categoria',blank=True, null=True)
    precioMayor = models.FloatField(verbose_name='Precio por mayor',blank=True, null=True,default=0)
    precio = models.FloatField(verbose_name='Precio',blank=True, null=True,default=0)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos',verbose_name='Imagen',blank=True, null=True,default='perfume.png')
    imagenes = models.ManyToManyField(ImagenProducto, null=True, blank=True,verbose_name='Imagenes')
    stock = models.IntegerField(verbose_name='Stock', blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateField(auto_now_add=True, verbose_name='Actualizado')

    def __str__(self):
        return self.nombre



