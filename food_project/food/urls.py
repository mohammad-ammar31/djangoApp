#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all_food', views.all_food, name='all_food'),
    path('add_food', views.add_food, name='add_food'),
    path('remove_food', views.remove_food, name='remove_food'),
    path('remove_food/<int:food_id>', views.remove_food, name='remove_food'),
    path('filter_food', views.filter_food, name='filter_food'),
]
