from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/',views.RegisterView.as_view()),
    path('logout/', views.logout),
]
