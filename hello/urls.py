from django.urls import path, include

from django.contrib import admin
from . import views
app_name = 'hello'
urlpatterns = [
    path('', views.drinks, name='drinks'),
    path('new_drinks/', views.new_drinks, name='new_drink'),
    # path('projects.html', views.projects, name='projects'),
    # path('drinks.html', views.drinks, name='drinks')
    
]