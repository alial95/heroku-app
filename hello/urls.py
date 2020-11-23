from django.urls import path, include

from django.contrib import admin
from . import views
urlpatterns = [
    path('new_entry.html', views.new_entry, name='new_entry'),
    path('projects.html', views.projects, name='projects'),
    # path('drinks.html', views.drinks, name='drinks')
    
]