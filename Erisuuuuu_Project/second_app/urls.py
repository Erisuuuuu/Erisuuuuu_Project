from django.urls import path,include
from . import views
from first_app.models import Other
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet, OtherViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'other', OtherViewSet)

urlpatterns = [
    path('product_list/',views.product_list,name='product_list'),
    path('', include(router.urls)),
    path('upload_image/', views.upload_image, name='upload_image'),
]