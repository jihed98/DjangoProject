from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from autenticazione.models import Person


class PersonCrispyForm(forms.ModelForm):
    helper = FormHelper()

    helper.form_id = 'person-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'save'))

    confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Person
        fields = ('username','mail', 'password')

    def clean(self):
        cleaned_data = super(PersonCrispyForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id:  # se esiste già l'id --> change
            self.helper.inputs[0].value = 'Update'
            self.helper.inputs[0].field_classes = 'btn btn-primary'
        else:  # create person
            self.helper.inputs[0].value = 'Create'
            self.helper.inputs[0].field_classes = 'btn btn-success'
    '''