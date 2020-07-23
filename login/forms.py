from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label_suffix="Nombre", label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu nickname o email', 'id': 'user'}   
    ))
    password = forms.CharField(label_suffix="Password", label="Password", required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Escribe tu contraseña', 'id': 'password'}   
    ))