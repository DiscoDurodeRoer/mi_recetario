from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

from .forms import LoginForm, RegisterForm

def login(request):
    
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/user')

    else:
        login_form = LoginForm()

    return render(request, 'auth/login.html', {'form': login_form})


def register(request):
    
    if request.method == "POST":

        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/users')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, "auth/register.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')