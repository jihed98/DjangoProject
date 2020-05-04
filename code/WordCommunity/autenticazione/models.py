from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.PROTECT)
    mail = models.EmailField()

    def __str__(self):
        return self.user.username

    @classmethod
    def create(cls, **kwargs):
        utente = cls(user=kwargs['user'], mail=kwargs['mail'])
        return utente

