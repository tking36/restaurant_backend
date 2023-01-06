from rest_framework import serializers 
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Restaurant # tell django which model to use
        fields = ('id', 'name', 'address', 'image', 'price', 'cuisine', 'number') # tell django which fields to include