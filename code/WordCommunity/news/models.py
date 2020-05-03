from django.db import models
from django.urls import reverse


class Utente(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome


# Create your models here.
class Articolo(models.Model):
    """il modello generico di un articolo """
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("articolo_deatil", kwargs={"pk": self.pk})

