from django.urls import path, include

from django.contrib import admin
from . import views
app_name = 'covid'
urlpatterns = [
    path('', views.index, name='covid'),
    # path('projects.html', views.projects, name='projects'),
    # path('drinks.html', views.drinks, name='drinks')
    
]