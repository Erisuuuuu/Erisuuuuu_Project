from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Category, Product, Review
from first_app.models import Other
from .serializers import (CategorySerializer, ProductSerializer, ReviewSerializer, OtherSerializer)
from .forms import UploadImageForm
from .models import UploadedImage
import uuid
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
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
# @login_required
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохранение картинки и информации о ней
            uploaded_image = form.save(commit=False)
            uploaded_image.user = request.user  # Текущий пользователь
            uploaded_image.save()
            return redirect('upload_image')  # Перенаправление на ту же страницу
    else:
        form = UploadImageForm()

    # Получаем все загруженные картинки текущего пользователя
    user_images = UploadedImage.objects.filter(user=request.user)
    return render(request, 'second_app/upload_image.html', {'form': form, 'user_images': user_images})