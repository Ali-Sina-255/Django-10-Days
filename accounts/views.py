from django.shortcuts import render, redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register_view(request):
    form  = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        confirm_password = form.clean_data.get('confirm_password')
        try: 
            user = User.objects.create_user(username, password,email)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            request.session['registration_errors']=  1


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request,user)
            return redirect('/home')
        else:
            return render(request,'product/forms.html' )
    context = {
        'form': form,
        'invalid_username': request.session.get('invalid-username'),
        'invalid_password': request.session.get('invalid-password'),
        'invalid_login': request.session.get('invalid-login'),
        'invalid_registration': request.session.get('invalid-registration'),
    }
    return render(request,'account/login.html', context)
def logout(request):
    logout(request)
    return redirect('/login')