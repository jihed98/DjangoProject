from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Articolo (models.Model):
    titolo = models.CharField(max_length=120)
    descrizione = models.TextField()
    lingua_sorgente = models.CharField(max_length=5, default="it")
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_articolo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articoli")
    indice = models.FloatField(default=0.0)
    is_listed = models.BooleanField(default=True) # default è pubblico

    
    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_view", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = 'Articoli'