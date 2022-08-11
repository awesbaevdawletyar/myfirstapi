from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductListSerializer
# Create your views here.

class ProductListAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer