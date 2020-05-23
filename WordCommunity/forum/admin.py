from django.contrib import admin
from .models import Articolo

# Register your models here.


class ArticoloModelAdmin(admin.ModelAdmin):
    model = Articolo
    list_display = ["titolo", "autore_articolo"]
    search_fields = ["titolo", "autore_articolo__username"]
    list_filter = ["data_creazione"]

'''
registriamo il modello Articolo e ArticoloModelAdmin
'''''
admin.site.register(Articolo,ArticoloModelAdmin)