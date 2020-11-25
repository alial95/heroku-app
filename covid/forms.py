from django import forms
from .models import AreaNames

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaNames
        fields = ['area']
        