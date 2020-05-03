from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mail = models.EmailField()

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return self.username
