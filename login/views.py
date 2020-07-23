from django.shortcuts import render
from .forms import LoginForm
from .models import User
from django.shortcuts import redirect

def login(request):

    msg_error = None

    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():

            user = request.POST.get('user', '')
            password = request.POST.get('password', '')

            num_users = User.objects.filter(nickname=user).filter(password__exact=password).count()

            if num_users == 1:
                return redirect('/user')
            else:
                msg_error = "Usuario o contraseña equivocados."

    else:
        login_form = LoginForm()



    return render(request, 'login/login.html', {'form': login_form, 'msg_error': msg_error})