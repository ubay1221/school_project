from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/', views.students_list, name='list'),
    path('create/', views.students_create, name='create'),
    path('detail/<int:pk>/', views.students_detail, name='detail'),
    path('delete/<int:pk>/', views.students_del, name='delete'),
]