from django.contrib import admin

# Register your models here.
from articolo.models import Articolo, WordList

admin.site.register(Articolo)
admin.site.register(WordList)
