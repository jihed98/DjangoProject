from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from autenticazione.forms import  RegisterForm


class UserCreateView(CreateView):
    template_name = 'registration/create_user.html'
    form_class = RegisterForm
    success_url = reverse_lazy('autenticazione:registration-fake')


def auth_home(request):
    return render(request, 'auth_home.html')

def home(request):
    return render(request, 'registration/fake.html')

def exit (request):
    return render(request, 'registration/fake2.html')
