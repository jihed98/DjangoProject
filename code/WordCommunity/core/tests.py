from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.test import TestCase
from accounts.views import registrazioneView

# Create your tests here.
from django.urls import reverse


class CoreTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='dummy', email='dummy@dummy.com', password='dummypassword')
        self.credential = {'username':'dummy', 'password':'dummypassword'}

    def test_login_required(self):
        '''test on login_required'''
        response = self.client.get('')
        self.assertRedirects(response,  '/accounts/login/?next=%2F')
        # 302 --> FOUND: pagina esiste ma non puoi entrarci
        self.assertEqual(response.status_code, 302)

    def test_homepage(self):
        self.client.login(**self.credential)
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)



