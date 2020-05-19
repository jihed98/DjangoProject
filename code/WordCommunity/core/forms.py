from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from accounts.models import UserProfile


class BlacklistForm (forms.ModelForm):


    class Meta:
        model = UserProfile
        fields = ()

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk')
        super().__init__(*args, **kwargs)
        self.profilo = UserProfile.objects.get(id=pk)
        self.fields['blacklist'] = forms.CharField(required=True)

    def clean(self):
        super().clean()
        text = self.cleaned_data['blacklist']
        self.profilo.appendBlacklist(text)
        self.profilo.save()
        return self.cleaned_data


