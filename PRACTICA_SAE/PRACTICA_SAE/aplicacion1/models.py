from django.db import models


''' SE DEFINE DOS MODELOS "CATEGORIA CON LLAVE PRIMARIA" Y "PRODUCTO CON LLAVE FORANEA" '''

class marca(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        db_table = 'Marca'
        ordering = ['id']

class category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcion')
    price = models.IntegerField(verbose_name='Precio')
    #category = models.ForeignKey(category, on_delete=models.CASCADE)
    category = models.ManyToManyField(category)
    marca = models.ForeignKey(marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        db_table = 'Producto'
        ordering = ['id'] #ordenar los registros que se organizan por su id 

