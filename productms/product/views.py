from typing import Generic
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import render, get_object_or_404
from product.serializers import CategorySerializer, ProductSerializer
 
from .models import Category, Product
 
 
# Create your views here.
 
class productview(Generic.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class cateforyview(Generic.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 