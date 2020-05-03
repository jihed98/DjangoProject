from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Utente(User):
    mail = models.EmailField

    class Meta:
        verbose_name_plural = 'Utenti'

    def __str__(self):
        return self.username
