from django.contrib.auth.models import User

from core.views import ArticoloChange
from forum.models import Articolo
from django.contrib.auth.views import LoginView
from django.test import TestCase
from accounts.views import registrazioneView

# Create your tests here.
from django.urls import reverse


class CoreTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='dummy', email='dummy@dummy.com', password='dummypassword')
        self.credential = {'username':'dummy', 'password':'dummypassword'}
        self.articolo = Articolo.objects.create(titolo = "Titolo Test",
                                                descrizione = ['test', 'parola', 'tetto'],
                                                autore_articolo=self.user)
        self.user2 = User.objects.create_user(username='dummy2', email='dummy@dummy.com', password='dummypassword')
        self.credential2 = {'username': 'dummy2', 'password': 'dummypassword'}

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

    def test_articolo_change(self):
        self.client.login(**self.credential)
        response = self.client.get('/articolo/' + str(self.articolo.id) +'/modifica/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/articolo/' + str(self.articolo.id) +'/modifica/', {})
        self.assertFormError(response, 'form', 'titolo', 'Questo campo è obbligatorio.')
        response = self.client.post('/articolo/' + str(self.articolo.id) + '/modifica/',
                                    {'titolo':'cambio titolo'})
        self.assertRedirects(response, '/user/' + self.user.username + '/')
