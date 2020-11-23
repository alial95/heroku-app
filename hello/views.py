from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DrinkForm
from .models import Greeting, Entry, Drinks

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
    
    drinks = Drinks.objects.all()
    return render(request, 'drinks.html', {'drinks': drinks})
def new_drinks(request):
    if request.method == "POST":  
        form = DrinkForm(request.POST)  
        if form.is_valid():  
            form.save()
        else:
            print('Form is incorrectly formatted') 
    else:  
        form = DrinkForm()  
    return render(request, 'new_drinks.html', {'form': form})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
