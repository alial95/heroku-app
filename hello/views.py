from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView
from .forms import DrinkForm, PersonForm
from .models import Greeting, Entry, Drinks, Sizes, Person
from django.contrib.auth import login

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
@login_required
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
            return redirect('new_person')
            
            
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

def logout(request):
    return render(request, 'logout.html')

class ViewUsers(ListView):
    model = User
    template_name = 'users.html'

class ViewPeople(ListView):
    model = Person
    template_name = 'show_people.html'

class ViewDrinks(ListView):
    model = Drinks
    template_name = 'show_drinks.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            new_user = form.save()
            login(request, new_user)
            return redirect('hello:drinks')
    else:  
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)