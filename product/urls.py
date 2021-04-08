from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('list/', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
    path('create/', views.ProductCreate.as_view()),
    
    path('api/product/', views.ProductListAPI.as_view()),
    path('api/product/<int:pk>/', views.ProductDetailAPI.as_view())
]
