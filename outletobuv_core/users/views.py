from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from users.models import User
from users.forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from django.contrib.auth.views import LoginView


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = '%(username)s was created successfully'
    title = 'Регистрация'
    

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
