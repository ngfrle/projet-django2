from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Etudiant, Administration

class EtudiantCreationForm(UserCreationForm):
    class Meta:
        model = Etudiant
        fields = ['email', 'username', 'matricule']

class AdministrationCreationForm(UserCreationForm):
    class Meta:
        model = Administration
        fields = ['email', 'username']

from django import forms
from .models import CustomUser

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import Doc

class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = ['nom', 'categorie', 'auteur', 'description', 'file']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



 

