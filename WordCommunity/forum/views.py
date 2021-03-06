from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Articolo
from . import textProcessor
import json


# Create your views here.


class CreaArticolo(CreateView):
    '''
    tramite la CreateView di Django, permette la creazione dell'articolo
    i campi che l'utente deve riempire sono il titolo,la descrizione(che è il testo dell'articolo)
    e la lunghezza_minima_delle_parole_che_si_vogliono_eliminare che di default è 0
    '''
    model = Articolo
    fields = ["titolo", "descrizione", "lunghezza_minima_delle_parole_che_si_vogliono_eliminare"]
    template_name = "forum/crea_articolo.html"

    def form_valid(self, form):
        form.instance.autore_articolo_id = self.request.user.pk
        # print(form.instance.descrizione)
        # qua si deve inserire lo script per la divisione in parole del descrizione
        d = textProcessor.textToDict(form.instance.descrizione,
                                     form.instance.lunghezza_minima_delle_parole_che_si_vogliono_eliminare)
        idx = textProcessor.getIndex(d)
        form.instance.descrizione = json.dumps(d)
        form.instance.indice = idx

        # Articolo.objects.create_articolo(form.instance.titolo, form.instance.descrizione, self.request.user)

        return super().form_valid(form)

    def get_success_url(self):
        pk = self.object.id
        success_url = reverse_lazy("articolo_view", kwargs={'pk': pk})
        return success_url


def visualizzaArticolo(request, pk):
    '''
    view per visualizzare i dettagli di un articolo
    :param pk: id dell'articolo di cui visualizzare i dettagli
    '''
    articolo = get_object_or_404(Articolo, pk=pk)
    text = json.loads(articolo.descrizione)
    utente = request.user.profile
    blacklist = utente.blacklist

    C = {k: v for k, v in text.items() if k not in blacklist}
    idx = textProcessor.getIndex(C)

    context = {"articolo": articolo, "parole": C, 'indice': idx}
    return render(request, "forum/articolo.html", context)


def visualizzaClassifica(request):
    '''
    view per mostrare tutte le parole presenti negli articoli del sito con le loro frequenze totali
    '''
    words = {}
    for a in Articolo.objects.all():
        words.update(json.loads(a.descrizione))
    utente = request.user.profile
    blacklist = utente.blacklist

    C = {k: v for k, v in words.items() if k not in blacklist}
    idx = textProcessor.getIndex(C)

    context = {"parole": C, 'indice': idx}

    return render(request, "forum/classifica.html", context)


def scegliArticoliView(request):
    '''
    view per selezionare due articoli da confrontare
    '''
    articoli = Articolo.objects.all()
    context = {"articoli": articoli}
    return render(request, "forum/scelta_confronto.html", context)


def confrontaArticoliView(request, pk1, pk2):
    '''
    view per confrontare due articoli. Per poter essere visualizzato bene sul template andiamo a costruire
    una lista di liste. Le liste interne sono strutturate così [frequenza_art1, termine, frequenza_art2 ]
    :param request:
    :param pk1:
    :param pk2:
    :return:
    '''
    art1 = Articolo.objects.get(id=pk1)
    art2 = Articolo.objects.get(id=pk2)

    txt1 = {k: v for k, v in art1.getDescrizione().items() if k not in request.user.profile.blacklist}
    txt2 = {k: v for k, v in art2.getDescrizione().items() if k not in request.user.profile.blacklist}

    idx1 = textProcessor.getIndex(txt1)
    idx2 = textProcessor.getIndex(txt2)

    bigL = []

    # k è la parola
    for k in txt1.keys():
        l = []
        if (k not in txt2.keys()):  # se non c'è in txt2
            l = [txt1[k], k, 0]
        else:  # in entrambi
            l = [txt1[k], k, txt2[k]]

        bigL.append(l)

    for k in txt2.keys():  # parole in 2 ma non in 1
        if (k not in txt1.keys()):
            l = [0, k, txt2[k]]
            bigL.append(l)

    context = {"art1": art1, "art2": art2, 'Biglist': bigL, 'idx1': idx1, 'idx2': idx2}

    return render(request, 'forum/confronta.html', context)
