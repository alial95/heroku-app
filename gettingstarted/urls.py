from django.urls import path, include

from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('', hello.views.new_entry, name='new_entry'),
    path('', hello.views.projects, name='projects'),
    path('', include('hello.urls'), name='hello'),
    path('drinks/', hello.views.drinks, name='drinks'),
    path('new_drinks/', hello.views.new_drinks, name='new_drink'),
    path('new_person/', hello.views.new_person, name='new_person'),
    path('users/', hello.views.ViewUsers.as_view(), name='users'),
    path('', include('django.contrib.auth.urls')),
    # path('logout/', hello.views.logout, name='logout')
]
