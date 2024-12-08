from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('list/', views.gorups_list, name='list'),
    path('create/', views.groups_create, name='create'),
    path('detail/<int:pk>/', views.groups_detail, name='detail'),
    path('delete/<int:pk>/', views.groups_del, name='delete'),
]
