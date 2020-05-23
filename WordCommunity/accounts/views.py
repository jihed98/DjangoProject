from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from accounts.forms import FormRegistrazione
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from accounts.models import UserProfile

'''
La funzione registrazioneView permette all'utente di registrasi al sito
Se il form è valid l'utente deve scrivere il suo username, la sua email
 e la sua password
'''
def registrazioneView(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            utente = User.objects.create_user(username=username, password=password, email=email)
            UserProfile.objects.create(user=utente)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = FormRegistrazione()   
    context = {"form":form}
    return render(request, 'accounts/registrazione.html', context)
