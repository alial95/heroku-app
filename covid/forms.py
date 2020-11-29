from django import forms
from .models import AreaNames, Regions

class AreaForm(forms.Form):
    model_choice = forms.ModelChoiceField(
        queryset = AreaNames.objects.all(),
        initial = 'Area',
        label="Please enter an area "
        )
class NationForm(forms.Form):
    model_choice = forms.ModelChoiceField(
        queryset = Regions.objects.all(),
        initial = 0,
        label="Please enter a nation "
        )