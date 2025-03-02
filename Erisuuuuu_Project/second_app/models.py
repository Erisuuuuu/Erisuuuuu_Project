from django.db import models
from first_app.models import Other
# Create your models here.

# Модель "Категория"
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название категории
    description = models.TextField(blank=True, null=True)  # Описание категории

    def __str__(self):
        return self.name

# Модель "Товар"
class Product(models.Model):
    name = models.CharField(max_length=200)  # Название товара
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Связь с категорией
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    description = models.TextField(blank=True, null=True)  # Описание товара
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления товара

    def __str__(self):
        return self.name

# Модель "Отзыв"
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Связь с товаром
    author_name = models.CharField(max_length=100)  # Имя автора отзыва
    text = models.TextField()  # Текст отзыва
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Рейтинг (от 1 до 5)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания отзыва

    def __str__(self):
        return f"Отзыв от {self.author_name} на {self.product.name}"