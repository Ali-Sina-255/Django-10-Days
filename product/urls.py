from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('products/', views.product_list, name='products'),
]
