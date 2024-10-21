from django.urls import path
from . import views

urlpatterns = [
    path('', views.corse_list, name='corse_list'),
    path('corse/<int:pk>/', views.corse_detail, name='corse_detail'),
    path('corse/add/', views.add_corse, name='add_corse'), 
    path('corse/add_material/', views.add_material, name='add_material'),
]