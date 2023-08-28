from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import (LoginView as LoginViewGeneric,
                                       LogoutView as LogoutViewGeneric,
                                       )

from django.urls import reverse_lazy
from django.views.generic import CreateView

from adverts.models import Advert
from .forms import AuthenticationForm, UserCreationForm


class LoginView(LoginViewGeneric):
    template_name = 'user_auth/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy("adverts:user-adverts")



class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("adverts")



class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_auth/register.html'
    success_url = reverse_lazy("adverts:user-adverts")

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user: AbstractUser = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response




