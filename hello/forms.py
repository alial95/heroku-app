from django import forms
from hello.models import Drinks, Sizes

class DrinkForm(forms.ModelForm): 
    name = Drinks.name
    size = Sizes.size
    price = Drinks.price