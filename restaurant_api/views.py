from django.shortcuts import render

from rest_framework import generics
from .serializers import RestaurantSerializer
from .models import Restaurant

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = RestaurantSerializer # tell django what serializer to use

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all().order_by('id')
    serializer_class = RestaurantSerializer