from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.BoardtDetail.as_view()),
    path('list/', views.BoardList.as_view()),
    path('write/', views.board_write)
]
