from django.urls import path, include

from django.contrib import admin
from . import views
app_name = 'covid'
urlpatterns = [
    path('covid/', views.covid_home, name='covid'),
    # path('projects.html', views.projects, name='projects'),
    # path('drinks.html', views.drinks, name='drinks')
    
]