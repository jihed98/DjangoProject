import json

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
        d = {'test':1, 'parola':1, 'tetto':1}
        self.articolo = Articolo.objects.create(titolo = "Titolo Test",
                                                descrizione = json.dumps(d),
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
        # con utente autenticato
        self.client.login(**self.credential)
        response = self.client.get('/articolo/' + str(self.articolo.id) +'/modifica/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/articolo/' + str(self.articolo.id) +'/modifica/', {})
        self.assertFormError(response, 'form', 'titolo', 'Questo campo è obbligatorio.')
        response = self.client.post('/articolo/' + str(self.articolo.id) + '/modifica/',
                                    {'titolo':'cambio titolo'})
        self.assertRedirects(response, '/user/' + self.user.username + '/')
        self.client.logout()

        # con utente non autenticato
        self.client.login(**self.credential2)
        response = self.client.get('/articolo/' + str(self.articolo.id) +'/modifica/')
        self.assertTemplateUsed(response, 'forum/articolo.html')
        self.assertTemplateNotUsed(response, 'core/modifica.html')

    def test_articolo_delete(self):
        # con utente autenticato
        self.client.login(**self.credential)
        response = self.client.get('/articolo/' + str(self.articolo.id) +'/delete/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/articolo/' + str(self.articolo.id) + '/delete/', {})
        self.assertRedirects(response, '/user/' + self.user.username + '/')
        self.client.logout()

        # con utente non autenticato
        self.client.login(**self.credential2)
        response = self.client.get('/articolo/' + str(self.articolo.id) +'/delete/')
        self.assertTemplateNotUsed(response, 'core/deletearticle.html')

    def test_userList(self):
        # con utente autenticato
        self.client.login(**self.credential)
        response = self.client.get('/users/')
        self.assertTemplateUsed(response, 'core/users.html')
        self.client.logout()

        # con utente autenticato
        response = self.client.get('/users/')
        self.assertTemplateNotUsed(response, 'core/users.html')

    def test_userProfileView(self):
        # con utente autenticato
        # su il tuo profilo
        self.client.login(**self.credential)
        response = self.client.get('/user/' + self.user.username + '/')
        self.assertTemplateUsed(response, 'core/profilo.html')
        self.assertTrue(response.status_code, 200)

        # sul profilo degli altri
        response = self.client.get('/user/' + self.user2.username + '/')
        self.assertTemplateNotUsed(response, 'core/profilo.html')
        self.assertTemplateUsed(response, 'core/user_profile.html')

        # con utente non autenticato
        self.client.logout()
        response = self.client.get('/user/' + self.user.username + '/')
        self.assertRedirects(response, '/accounts/login/?next=/user/' + self.user.username + '/')
