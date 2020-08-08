from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label_suffix="Nombre", label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu nickname o email', 'id': 'username'}   
    ))
    password = forms.CharField(label_suffix="Password", label="Password", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu contraseña', 'id': 'password'}   
    ))

class RegisterForm(UserCreationForm):
    username = forms.CharField(label_suffix="Nombre", label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu nickname o email', 'id': 'username'}   
    ))
    password1 = forms.CharField(label_suffix="Password", label="Password", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu contraseña', 'id': 'password1'}   
    ))
    password2 = forms.CharField(label_suffix="Confirmar password", label="Confirmar password", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe de nuevo tu contraseña', 'id': 'password2'}   
    ))