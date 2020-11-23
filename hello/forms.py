from django import forms
from hello.models import Drinks, Sizes

class DrinkForm(forms.ModelForm): 
    class Meta:
        model = Drinks, Sizes
        fields = '__all__'