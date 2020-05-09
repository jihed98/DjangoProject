from django.test import TestCase

import json

from django.test import TestCase
from django.contrib.auth.models import User
from forum.models import Articolo
from forum import textProcessor


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

    def test_indice (self):
        ix1 = textProcessor.getIndex(textProcessor.textToDict('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                                              'Nullam et urna at justo ornare sodales.Fusce nec ex non '
                                                              'quam fringilla lobortis.Vestibulum porttitor quam eget '
                                                              'enim luctus porta.Integer sed erat quis felis feugiat varius.'
                                                              'Nam vitae mi et velit placerat vulputate.Nunc vestibulum '
                                                              'eros id eleifend elementum.Etiam ut massa egestas, ornare'
                                                              ' tortor vitae, eleifend mi.'))

        ix2 = textProcessor.getIndex(textProcessor.textToDict('Sed at leo vitae metus pulvinar eleifend at eget lorem. '
                                                              'Morbi porttitor nisl non enim ultricies, molestie elementum'
                                                              ' est varius. Nunc eu mauris a est eleifend '
                                                              'accumsan.Morbi faucibus lacus non massa ullamcorper blandit.'))

        ix3 = textProcessor.getIndex(textProcessor.textToDict('questa stringa è bellissima'))
        ix4 = textProcessor.getIndex(textProcessor.textToDict('AAAAAAAA AAAAAAA'))
        ix5 = textProcessor.getIndex(textProcessor.textToDict('Ai  sensi  dell art.  79  del  testo  unico  delle  '
                                                              'disposizioni legislative  in  materia  doganale,  '
                                                              'approvato  con  il  decreto  del Presidente della '
                                                              'Repubblica 23 gennaio 1973, n. 43,  come  sostituito '
                                                              'dall art. 5, comma 2, della legge 25 luglio 2000, n. 213, '
                                                              ' il  saggiodi  interesse  per  il  pagamento  differito  '
                                                              'dei  diritti   doganalieffettuato oltre il periodo  di '
                                                              ' giorni  trenta  e stabilito  nella misura dello 0,213 '
                                                              'per cento annuo per il periodo dal 13 gennaio 2020 al 12 luglio 2020. '
                                                              'Il presente decreto sarà pubblicato nella Gazzetta Ufficiale'
                                                              ' della Repubblica italiana.'))

        print(ix1, ix2, ix3, ix4, ix5)
        self.assertGreaterEqual(ix1, ix2)
        self.assertGreater(ix1, ix3, msg="Problema")
        self.assertGreater(ix3, ix4, msg="Problema 2")
        self.assertGreater(ix5, ix4)

