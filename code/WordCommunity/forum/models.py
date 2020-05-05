from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Articolo (models.Model):
    titolo = models.CharField(max_length=120)
    descrizione = models.TextField()
    lingua_sorgente = models.CharField(max_length=4)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore_articolo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articoli")
    
    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_view", kwargs={"pk": self.pk})

# Create your models here.
class Meta:
    verbose_name = "Articolo"
    verbose_name_plural = "Articoli"
