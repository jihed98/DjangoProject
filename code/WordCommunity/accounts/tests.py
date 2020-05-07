from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse


class LogInTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        #self.factory = RequestFactory()
        self.dummy_user = User.objects.create_user(username='dummy', password='nothings')
        self.dummy_user2 = User.objects.create_user(username='dummy2', password='nothing')

    def test_login(self):
        #dummy_thing = Thing.objects.get(name="Dummy Book")
        self.client.login(username=self.dummy_user2.username, password='nothing')

        # Test POST invalid data
        response = self.client.post('/accounts/registrazione/', {})
        self.assertFormError(response, 'form', 'username', 'Questo campo è obbligatorio.')
        self.assertFormError(response, 'form', 'email', 'Questo campo è obbligatorio.')
        self.assertFormError(response, 'form', 'password1', 'Questo campo è obbligatorio.')
        self.assertTemplateUsed(response, 'accounts/registrazione.html')
        self.assertEqual(response.status_code, 200)

        # Test POST valid data?
        #response = self.client.post('/accounts/create_thing/',
                                   # {'name': 'new name', 'description': 'new description', })
        #self.assertEqual(response.status_code, 200)