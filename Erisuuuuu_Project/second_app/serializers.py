from rest_framework import serializers
from .models import Category, Product, Review
# from ..first_app.models import Other
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Сериализуем все поля модели

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# class OtherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Other
#         fields = '__all__'