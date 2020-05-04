from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from autenticazione.models import  Author


class RegisterForm(UserCreationForm):
    mail = forms.EmailField(label = 'email')

    class Meta:
        model = User
        fields = ('username', 'mail')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
            author = Author.create(user = user , mail = self.cleaned_data['mail'])
            author.save()
        return user


