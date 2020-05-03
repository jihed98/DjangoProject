from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo, Utente

#def homepage(request):
   # return HttpResponse("HOMEPAGE")

#def homepage(request):
    #a = []
    #g = []

    #for art in Articolo.objects.all():
        #a.append(art.titolo)

    
    #response =str(a) + "<br>" + str(g)
    #print(response)

    #return HttpResponse("<h1>" + response + "<h1>")

def home(request):
    articoli = Articolo.objects.all()
    utenti = Utente.objects.all()
    context = {"utenti": utenti, "articoli": articoli}
    print(context)
    return render(request,"homepage.html",context)


def articoloDetailView(request,pk):
    articolo = get_object_or_404(Articolo,pk=pk)
    context = {"articolo": articolo}
    return render(request,"articolo_detail.html",context)