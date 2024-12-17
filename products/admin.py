from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display= ['name', 'price'] #modificar la vista del admin
    search_fields= ['name']#agregar un buscador a la vista 

admin.site.register(Product,ProductAdmin)#para administrar los productor desde el admin 