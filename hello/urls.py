from django.urls import path, include

from django.contrib import admin
from . import views
app_name = 'hello'
urlpatterns = [
    path('', views.drinks, name='drinks'),
    path('new_drinks/', views.new_drinks, name='new_drink'),
    path('new_person/', views.new_person, name='new_person'),
    path('show_drinks/', views.ViewDrinks.as_view(), name='display_drinks'),
    path('show_people/', views.ViewPeople.as_view(), name='display_people'),
    
]