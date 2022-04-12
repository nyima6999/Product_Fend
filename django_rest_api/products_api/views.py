from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ProductSerializer # tell django what serializer to use

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer