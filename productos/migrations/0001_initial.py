# Generated by Django 3.1.7 on 2022-06-12 19:59

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nombre', unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='nombre')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='productos.caracteristica')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200, verbose_name='color')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='prouctos', verbose_name='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='genero')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='products/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200, verbose_name='marca')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='prouctos', verbose_name='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField(blank=True, null=True, verbose_name='Codigo')),
                ('nombre', models.CharField(max_length=200, verbose_name='Producto')),
                ('precioMayor', models.FloatField(blank=True, default=0, null=True, verbose_name='Precio por mayor')),
                ('precio', models.FloatField(blank=True, default=0, null=True, verbose_name='Precio')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, default='perfume.png', null=True, upload_to='productos', verbose_name='Imagen')),
                ('stock', models.IntegerField(blank=True, verbose_name='Stock')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='Actualizado')),
                ('caracteristica', models.ManyToManyField(blank=True, null=True, to='productos.Caracteristica', verbose_name='Tallas')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.genero', verbose_name='Categoria')),
                ('colores', models.ManyToManyField(blank=True, null=True, to='productos.Color', verbose_name='Colores')),
                ('imagenes', models.ManyToManyField(blank=True, null=True, to='productos.ImagenProducto', verbose_name='Imagenes')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.marca', verbose_name='Marca')),
            ],
        ),
    ]
