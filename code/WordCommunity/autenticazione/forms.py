from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm

from autenticazione.models import Utente


class RegisterForm(UserCreationForm):
    mail = forms.EmailField(label = 'email')

    class Meta:
        model = Utente
        fields = ('username', 'mail')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.mail = self.cleaned_data["mail"]
        if commit:
            user.save()
        return user

