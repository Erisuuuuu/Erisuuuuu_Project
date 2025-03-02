from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, Review
# from  import Other
from .serializers import (CategorySerializer, ProductSerializer, ReviewSerializer)
# , OtherSerializer)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
# class OtherViewSet(viewsets.ModelViewSet):
#     queryset = Other.objects.all()
#     serializer_class = OtherSerializer