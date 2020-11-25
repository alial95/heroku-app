from django import forms
from hello.models import Drinks, Sizes, Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DrinkForm(forms.ModelForm): 
    class Meta:
        model = Drinks
        fields = '__all__'

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user