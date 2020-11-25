from django.shortcuts import render

# Create your views here.
def covid_home(request):
    return render(request, 'covid_home.html',)