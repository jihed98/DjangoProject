from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from accounts.forms import FormRegistrazione


class LogInTest(TestCase):
    def setUp(self):
        self.dummy_user = User.objects.create_user(username='dummy', password='nothings', email='dummy@dummy.com')


    def test_registrazione(self):
        # Test POST invalid data
        response = self.client.post('/accounts/registrazione/', {})
        self.assertFormError(response, 'form', 'username', 'Questo campo è obbligatorio.')
        self.assertFormError(response, 'form', 'email', 'Questo campo è obbligatorio.')
        self.assertFormError(response, 'form', 'password1', 'Questo campo è obbligatorio.')
        self.assertTemplateUsed(response, 'accounts/registrazione.html')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/accounts/registrazione/', {'username':self.dummy_user.username, 'email':self.dummy_user.email,
                                                                 'password1':'vigorsol', 'password2':'wrong'})

        self.assertFormError(response, 'form', 'password2', 'I due campi password non corrispondono.')


        form_data = {'username':'user', 'email':'mail','password1':'vigorsol', 'password2':'vigorsol'}
        form = FormRegistrazione(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login(self):
        fake_credential = {'username':'ciao', 'password':'ciao'}
        true_credential = {'username':'dummy', 'password':'nothings'}
        t_cred = self.client.login(**true_credential)
        f_cred = self.client.login(**fake_credential)

        self.assertTrue(t_cred)
        self.assertFalse(f_cred)
