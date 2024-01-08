from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse_lazy

from common.views import TitleMixin
from users.models import User

from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView, CreateView

from users.forms import UserLoginForm, UserProfileForm, UserRegisterForm


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'
    success_url = reverse_lazy('home')


class UserProfileView(TitleMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class UserRegisterView(TitleMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    title = 'Регистрация'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super(UserRegisterView, self).form_valid(form)
        login(self.request, self.object)
        return valid