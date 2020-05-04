from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from articolo.models import Articolo

from autenticazione.models import Author


class ArticleCrispyForm(forms.ModelForm):
    testo = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    helper = FormHelper()

    # helper.form_id = 'person-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'save'))

    class Meta:
        model = Articolo
        fields = ('titolo',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ArticleCrispyForm, self).__init__(*args, **kwargs)
        self.helper.inputs[0].value = 'Create'
        self.helper.inputs[0].field_classes = 'btn btn-success'

    def save(self, commit=True):
        articolo = super(ArticleCrispyForm, self).save(commit=False)
        if commit:
            articolo = Articolo.create(titolo=self.cleaned_data['titolo'], author=self.cleaned_data['user'])
            articolo.save()
        return articolo



