import json

from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from forum.models import Articolo


class ArticoloTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='dummy', email='dummy@dummy.com', password='dummypassword')
        self.credential = {'username':'dummy', 'password':'dummypassword'}
        d = {'test':1, 'parola':1, 'tetto':1}
        self.articolo = Articolo.objects.create(titolo = "Titolo Test",
                                                descrizione = json.dumps(d),
                                                autore_articolo=self.user)
        self.user2 = User.objects.create_user(username='dummy2', email='dummy@dummy.com', password='dummypassword')
        self.credential2 = {'username': 'dummy2', 'password': 'dummypassword'}

    def test_visualizzaArticolo(self):
        self.client.login(**self.credential)
        response = self.client.get('/forum/articolo/' + str(self.articolo.id) + '/')
        self.assertTemplateUsed('forum/articolo.html')
        self.assertEqual(response.status_code, 200)

    def test_CreaArticolo(self):
        self.client.login(**self.credential)
        response = self.client.post('/forum/nuovo-articolo/', {})
        self.assertFormError(response, 'form', 'titolo', 'Questo campo è obbligatorio.')
        self.assertFormError(response, 'form', 'descrizione', 'Questo campo è obbligatorio.')
        self.assertTemplateUsed(response, 'forum/crea_articolo.html')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/forum/nuovo-articolo/', { 'titolo' : 'nuovo titolo',
                                                                'descrizione' : 'Questa stringa è bellissima'})
        self.assertRedirects(response, '/')