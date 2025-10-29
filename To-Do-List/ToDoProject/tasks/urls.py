from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
