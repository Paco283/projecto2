from django.shortcuts import render

# Create your views here.

# views.py
from rest_framework import generics
from .models import Productos
from .serializers import ProductSerializer

# Listar y Crear Productos
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductSerializer

# Detalle, Actualizar y Eliminar un Producto
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductSerializer
