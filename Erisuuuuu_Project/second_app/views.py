from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Product, Review
from first_app.models import Other
from .serializers import (CategorySerializer, ProductSerializer, ReviewSerializer, OtherSerializer)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class OtherViewSet(viewsets.ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    reviews = Review.objects.all()
    other = Other.objects.all()
    context = {
        'categories': categories,  # обратите внимание на регистр: используйте то же, что и в шаблоне
        'products': products,
        'reviews': reviews,
        'other': other,
    }
    return render(request, 'second_app/product_list.html', context)