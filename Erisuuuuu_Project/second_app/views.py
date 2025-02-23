from django.shortcuts import render
from .models import Category, Product, Review  # Импортируем модели

def product_list(request):
    # Получаем все категории, товары и отзывы
    categories = Category.objects.all()
    products = Product.objects.all()
    reviews = Review.objects.all()

    # Передаем данные в шаблон
    context = {
        'categories': categories,
        'products': products,
        'reviews': reviews,
    }

    # Рендерим шаблон с данными
    return render(request, 'second_app/product_list.html', context)