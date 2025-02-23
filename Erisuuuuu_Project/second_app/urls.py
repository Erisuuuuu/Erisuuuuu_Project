from django.urls import path
from . import views
# from ..Erisuuuuu_Project.urls import urlpatterns

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Связываем URL с представлением
]