from django.urls import path
from . import views
# from ..Erisuuuuu_Project.urls import urlpatterns

urlpatterns = [
    path('',views.index,name ='index'),
]