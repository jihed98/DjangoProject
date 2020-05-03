from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/create_user.html'
    success_url =  reverse_lazy('')