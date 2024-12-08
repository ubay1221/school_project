from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.teachers_list, name='list'),
    path('create/', views.teachers_create, name='create'),
    path('detail/<int:pk>/', views.teachers_detail, name='detail'),
    path('delete/<int:pk>/', views.teachers_del, name='delete'),
]