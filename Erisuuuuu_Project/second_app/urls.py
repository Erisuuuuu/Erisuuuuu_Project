from django.urls import path,include
from . import views
# from ..first_app.models import Other
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
# router.register(r'other', OtherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]