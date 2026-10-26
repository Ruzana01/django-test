from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('export-tests/', views.export_tests_to_word, name='export_tests'),
]