from django import forms
from .models import Product

class ProductForm(forms.Form): #formulario 
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    avilable = forms.BooleanField(initial=True, label="Disponible",required=False)
    photo = forms.ImageField(label="Foto", required=False)
    date_created = forms.DateTimeField(label="Fecha de creación")

    def save(self): #metodo de guardar, por medio de un diccionario
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            avilable=self.cleaned_data["avilable"],
            photo=self.cleaned_data["photo"],
            date_created=self.cleaned_data["date_created"],
        )