from django.contrib import admin

# Register your models here.

from .models import Drinks, Profile

admin.site.register(Drinks)
admin.site.register(Profile)