from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('list/', views.OrderList.as_view()),
    path('create/', views.OrderCreate.as_view()),
]
