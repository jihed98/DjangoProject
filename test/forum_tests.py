from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from forum.models import Articolo


class ArticoloTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test')
        user = get_object_or_404(User, username='test')
        Articolo.objects.create(titolo='testtitolo', autore_articolo=user)

    def test_articolo(self):
        articolo = Articolo.objects.get(titolo='testtitolo')
        self.assertEqual(articolo.titolo, 'testtitolo')

    def test_utente(self):
        utente = User.objects.get(username="test")
        self.assertEqual(utente.username, 'test')
