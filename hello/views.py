from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import DrinkForm, PersonForm
from .models import Greeting, Entry, Drinks, Sizes
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def new_entry(request):
    return render(request, 'new_entry.html')

def projects(request):
    return render(request, 'projects.html')
# def new_topic(request):
def drinks(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = DrinkForm()
    
    # drinks = Drinks.objects.all()
    return render(request, 'drinks.html')
def new_drinks(request):
    if request.method == "POST":  
        form = DrinkForm(request.POST)  
        if form.is_valid():  
            form.save()
        else:
            print('Form is incorrectly formatted') 
    else:  
        form = DrinkForm()  
    sizes = Sizes.objects.all()
    return render(request, 'new_drinks.html', {'form': form, 'sizes': sizes})

def new_person(request):
    context = {}
    if Drinks.objects.all():
        drinks = Drinks.objects.all()
        context['drinks'] = drinks

    if request.method == "POST":  
        form = PersonForm(request.POST)  
        if form.is_valid():  
            form.save()
        else:
            print('Form is incorrectly formatted') 
    else:  
        form = PersonForm()
        context['form'] = form
    return render(request, 'new_person.html', context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

class ViewUsers(ListView):
    model = User
    template_name = 'users.html'