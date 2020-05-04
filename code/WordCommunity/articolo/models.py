from datetime import datetime


from django.db import models

# Create your models here.
from django.db.models import PROTECT , CASCADE

from autenticazione.models import Author


class Articolo(models.Model):
    titolo = models.CharField(max_length=50 )
    author  = models.ForeignKey( Author,on_delete=PROTECT, related_name='autore')
    indice = models.FloatField()
    data  = models.DateTimeField(default=datetime.now())
    is_public = models.BooleanField(default=True)

class WordList(models.Model):
    word = models.CharField(max_length=20)
    frequenza = models.IntegerField()
    ref_articolo = models.ForeignKey(Articolo,on_delete= CASCADE, related_name= 'articolo')





