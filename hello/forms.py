from django import forms
from hello.models import Drinks

class DrinkForm(forms.ModelForm): 
    class Meta:
        model = Drinks
        fields = '__all__'