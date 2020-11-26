from django import forms
from .models import AreaNames

class AreaForm(forms.Form):
    model_choice = forms.ModelChoiceField(
        queryset = AreaNames.objects.all(),
        initial = 'Area',
        label="Please enter an area "
        )