import json

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


def strToDict (s):
    if s=='':
        d = dict()
    else:
        d = json.loads(s)
    return d


class Articolo(models.Model):
    '''
    modello per l'articolo. La descrizione viene salvata in un textfield ma è in un formato JSon, questo comporta
    operazioni di load e dump prima di prendersi le parole e di salvarle rispettivamente
    '''
    titolo = models.CharField(max_length=120)
    descrizione = models.TextField()
    lingua_sorgente = models.CharField(max_length=5, default="it")
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_articolo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articoli")
    indice = models.FloatField(default=0.0)
    is_listed = models.BooleanField(default=True)  # default è pubblico
    lunghezza_minima_delle_parole_che_si_vogliono_eliminare = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_view", kwargs={"pk": self.pk})

    def getDescrizione (self):
        d = strToDict(self.descrizione)
        return d

    class Meta:
        verbose_name_plural = 'Articoli'


