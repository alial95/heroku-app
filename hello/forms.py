from django import forms
from hello.models import Drinks, Sizes, Person

class DrinkForm(forms.ModelForm): 
    class Meta:
        model = Drinks
        fields = '__all__'

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'