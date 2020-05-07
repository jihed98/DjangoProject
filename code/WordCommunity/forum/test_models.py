from unittest import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Articolo


class ArticoloTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='test', mail='test@test.com')
        user = get_object_or_404(User, username='test')
        Articolo.objects.create(titolo='testtitolo', autore_articolo=user.id)

    def test_articolo(self):
        articolo = Articolo.objects.get(titolo='testtitolo')
        self.assertEqual(articolo.titolo, 'testtitolo')

