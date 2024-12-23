from rest_framework.serializers import ModelSerializer
from .models import Product

#los serializers son como un modelo de datos que se utiliza para comunicar con el front, de un modelo a un json o un xml
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'avilable', 'photo', 'date_created'] #campos que se van a mostrar en el json para comunicar con el front