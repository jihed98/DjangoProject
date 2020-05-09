import json

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from forum import textProcessor


class ArticoloManager (models.Manager):
    def create_articolo (self, titolo, descrizione, user):
        d = textProcessor.textToDict(descrizione)
        descrizione = json.dumps(d)
        #calcola indice
        self.autore_articolo_id = user.pk
        self.create(titolo=titolo, descrizione=descrizione, autore_articolo=user)
        #self.create(titolo=titolo, descrizione=descrizione, autore_articolo=user, indice = indice)


class Articolo(models.Model):
    titolo = models.CharField(max_length=120)
    descrizione = models.TextField()
    lingua_sorgente = models.CharField(max_length=5, default="it")
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_articolo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articoli")
    indice = models.FloatField(default=0.0)
    is_listed = models.BooleanField(default=True)  # default è pubblico

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_view", kwargs={"pk": self.pk})

    objects = ArticoloManager()

    class Meta:
        verbose_name_plural = 'Articoli'
