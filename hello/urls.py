from django.urls import path, include

from django.contrib import admin
from . import views
app_name = 'hello'
urlpatterns = [
    path('', views.drinks, name='drinks'),
    # path('projects.html', views.projects, name='projects'),
    # path('drinks.html', views.drinks, name='drinks')
    
]