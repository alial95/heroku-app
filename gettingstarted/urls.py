from django.urls import path, include

from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()
import covid.views
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
    path('drinks/', hello.views.drinks, name='drinks'),
    path('new_drinks/', hello.views.new_drinks, name='new_drink'),
    path('new_person/', hello.views.new_person, name='new_person'),
    path('users/', hello.views.ViewUsers.as_view(), name='users'),
    path('', include('django.contrib.auth.urls')),
    path('register/', hello.views.register, name='register'),
    path('show_drinks/', hello.views.ViewDrinks.as_view(), name='display_drinks'),
    path('show_people/', hello.views.ViewPeople.as_view(), name='display_people'),
    path('covid/', covid.views.covid_home, name='covid')
]
