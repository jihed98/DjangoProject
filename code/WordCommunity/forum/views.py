from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Articolo
from . import textProcessor
import json


# Create your views here.


class CreaArticolo(CreateView):
    model = Articolo
    fields = ["titolo", "descrizione",]
    template_name = "forum/crea_articolo.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.autore_articolo_id = self.request.user.pk
        print(form.instance.descrizione)
        # qua si deve inserire lo script per la divisione in parole del testo
        d = textProcessor.textToDict(form.instance.descrizione)
        form.instance.descrizione = json.dumps(d)

        #Articolo.objects.create_articolo(form.instance.titolo, form.instance.descrizione, self.request.user)

        return super().form_valid(form)


def visualizzaArticolo(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    text = json.loads(articolo.descrizione)
    indice = textProcessor.getIndex(text)
    context = {"articolo": articolo, "parole": text, "index":indice}
    return render(request, "forum/articolo.html", context)



