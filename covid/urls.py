from django.urls import path, include

from django.contrib import admin
from . import views
app_name = 'covid'
urlpatterns = [
    path('', views.covid_home, name='covid'),
    path('nations/', views.nation_select, name='nations')
    
]