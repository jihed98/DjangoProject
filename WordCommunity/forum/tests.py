from django.test import TestCase

import json

from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import UserProfile
from forum.models import Articolo
from forum import textProcessor


class ArticoloTestCase(TestCase):
    '''
    Questa classe serve per testare le funzionalità di articolo
    '''

    def setUp(self):
        '''
        Creiamo due utenti, due articoli e due user profile
        '''
        self.user = User.objects.create_user(username='dummy', email='dummy@dummy.com', password='dummypassword')
        self.credential = {'username':'dummy', 'password':'dummypassword'}
        d = {'test':1, 'parola':1, 'tetto':1}
        self.articolo = Articolo.objects.create(titolo = "Titolo Test",
                                                descrizione = json.dumps(d),
                                                autore_articolo=self.user)

        self.articolo2 = Articolo.objects.create(titolo = "Titolo Test2",
                                                descrizione = json.dumps(d),
                                                autore_articolo=self.user)

        self.user2 = User.objects.create_user(username='dummy2', email='dummy@dummy.com', password='dummypassword')
        self.credential2 = {'username': 'dummy2', 'password': 'dummypassword'}
        profilo1 = UserProfile.objects.create(user=self.user)
        profilo2 = UserProfile.objects.create(user=self.user2)


    def test_visualizzaArticolo(self):
        '''
        Ci accertiamo che l'utente riesca a visualizzare il suo articolo creato
        '''
        self.client.login(**self.credential)
        response = self.client.get('/forum/articolo/' + str(self.articolo.id) + '/')
        self.assertTemplateUsed(response, 'forum/articolo.html')
        self.assertEqual(response.status_code, 200)


    def test_CreaArticolo(self):
        '''
        Verifichiamo che nella creazione articolo i campi obbligatori siano necessari
        per la registrazione di un articolo
        Ci accertiamo che il template utilizzato sia quello giusto e che lo status code sia 200
        Proviamo ad inserire un articolo con credenziali valide e ci accertiamo che
        il tamplate utilizzato sia quello corretto
        '''
        self.client.login(**self.credential)
        response = self.client.post('/forum/nuovo-articolo/', {})
        self.assertFormError(response, 'form', 'titolo', 'Questo campo è obbligatorio.')
        self.assertFormError(response, 'form', 'descrizione', 'Questo campo è obbligatorio.')
        self.assertTemplateUsed(response, 'forum/crea_articolo.html')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/forum/nuovo-articolo/', { 'titolo' : 'nuovo titolo',
                                                                'descrizione' : 'Questa stringa è bellissima'})
        self.assertTemplateUsed('forum/articolo.html')

    def test_indice_base(self):
        s1 = textProcessor.getIndex(textProcessor.textToDict("A"))
        s2 = textProcessor.getIndex(textProcessor.textToDict("AA"))
        s3 = textProcessor.getIndex(textProcessor.textToDict("AAA"))
        s4 = textProcessor.getIndex(textProcessor.textToDict("A A"))
        s5 = textProcessor.getIndex(textProcessor.textToDict("A B"))
        s6 = textProcessor.getIndex(textProcessor.textToDict("A A A"))
        s7 = textProcessor.getIndex(textProcessor.textToDict("A B C"))
        s8 = textProcessor.getIndex(textProcessor.textToDict("ciao ciao ciao"))
        s9 = textProcessor.getIndex(textProcessor.textToDict("cio com sta"))
        s10 = textProcessor.getIndex(textProcessor.textToDict("ciaociao ciaociao ciaociao"))
        s11 = textProcessor.getIndex(textProcessor.textToDict("ciacia comcom stasta"))
        s12 = textProcessor.getIndex(textProcessor.textToDict("aaaa aaaa aaaa aaaa aaaa aaaa aaaa aaaa"))
        s13 = textProcessor.getIndex(textProcessor.textToDict("abcde fghij klmno"))
        print(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13)
        self.assertGreater(s7, s6, "0")
        self.assertGreater(s2, s1, "1")
        self.assertGreater(s3, s2, "2")
        self.assertGreater(s5, s4, "3")
        self.assertGreater(s3, s5, "4")
        self.assertGreater(s9, s8, "5")
        self.assertGreater(s11, s10, "6")
        self.assertGreater(s13, s12, "7")
        self.assertEqual(s5, s6, "tricky equal")



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


    def test_visualizzaClassifica(self):
        '''
        Ci accertiamo che l'utente sia registrato al sito e che possa visualizzare la
        classifica in maniera corretta, tramite il template corretto
        poi si controlla che un utente non registrato non possa visualizzare la classifica
        '''
        self.client.login(**self.credential)
        response = self.client.get('/forum/classifica/')
        self.assertTemplateUsed(response, 'forum/classifica.html')
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get('/forum/classifica/')
        self.assertTemplateNotUsed(response, 'forum/classifica.html')
        self.assertEqual(response.status_code, 302)

    def test_scegliArticoliView(self):
        '''
        si controlla che un utente registrato possa visualizzare corettamente
        la scelta degli atricoli da confrontare mentre un guest no
        '''
        self.client.login(**self.credential)
        response = self.client.get('/forum/articolo/confronta/')
        self.assertTemplateUsed(response, 'forum/scelta_confronto.html')
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get('/forum/articolo/confronta/')
        self.assertTemplateNotUsed(response, 'forum/scelta_confronto.html')
        self.assertEqual(response.status_code, 302)

    def test_confrontaArticoliView(self):
        '''
        Controlliamo che i due articoli creati nel setUp posso essre confrontati da un utente
        ma non da un guest
        '''
        self.client.login(**self.credential)
        response = self.client.get('/forum/articolo/confronta/' + str(self.articolo.id) + '/' + str(self.articolo2.id) + '/')
        self.assertTemplateUsed(response, 'forum/confronta.html')
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get('/forum/articolo/confronta/' + str(self.articolo.id) + '/' + str(self.articolo2.id) + '/')
        self.assertTemplateNotUsed(response, 'forum/confronta.html')
        self.assertEqual(response.status_code, 302)