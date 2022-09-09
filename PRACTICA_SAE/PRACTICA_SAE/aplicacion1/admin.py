from django.contrib import admin
from . models import category,Product, marca

admin.site.register(category) #se registra categoria 
admin.site.register(Product) # se registra producto
admin.site.register(marca) # se registra marca