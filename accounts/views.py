from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth.views import LoginView
from accounts.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy


class Register(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')


class Login(LoginView):
    template_name = 'login.html'
    success_url = '/'
    form_class = LoginForm 

def user_profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user' : user,
    }
    return render(request, 'user-profile.html', context)

