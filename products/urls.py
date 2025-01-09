from django.urls import path
from .views import ProductListView, ProductDetailView , CategoryListView, CategoryDetailView

urlpatterns = [
    path('categories/', ProductListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', ProductDetailView.as_view(), name='category-detail'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]