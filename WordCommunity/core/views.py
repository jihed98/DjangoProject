from django.core.serializers import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, DetailView, FormView
from django.views.generic.list import ListView

from accounts.models import UserProfile
from core.forms import BlacklistForm
from forum.models import Articolo

# Create your views here.
# def homepage(request):
#   return render(request, 'core/homepage.html')
from forum.views import visualizzaArticolo


class HomeView(ListView):
    '''
    Visualizza la Homepage del sito, mostrando gli articoli in ordine dal piu recente
    '''
    queryset = Articolo.objects.all().order_by("-pk")
    template_name = 'core/homepage.html'
    context_object_name = "lista_articoli"


def cerca(request, ):
    '''
    Barra di ricerca
    :return: ritorna la pagina che mostra i risultati della ricerca
    '''
    if "q" in request.GET:
        querystring = request.GET.get("q")
        # print(querystring)
        if len(querystring) == 0:
            return redirect("/cerca/")
        articoli = Articolo.objects.filter(titolo__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        # print(users)
        context = {"articoli": articoli, "users": users}
        return render(request, 'core/cerca.html', context)
    else:
        return render(request, 'core/cerca.html')


def userProfileView(request, username, ):
    '''
    Visualizza la pagina del profilo utente
    :param username: nome dell'utente
    :return: rotorna la pagina del profilo utente
    '''
    if request.user.username != username:
        return altriuserProfileView(request, username)
    user = get_object_or_404(User, username=username)
    articoli_utente = Articolo.objects.filter(autore_articolo=user.pk).order_by("-pk")
    context = {"user": user, "articoli_utente": articoli_utente}
    return render(request, 'core/profilo.html', context)


class UserList(ListView):
    '''
    Lista degli utenti
    '''
    model = User
    template_name = 'core/users.html'


class ArticleDelete(DeleteView):
    '''
    Eliminazione di un articolo
    '''
    model = Articolo
    template_name = 'core/deletearticle.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Articolo, id=articleid)

        if user.id is not articolo.autore_articolo.id:
            return visualizzaArticolo(request, articleid)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Articolo, id=articleid)
        user = get_object_or_404(User, username=articolo.autore_articolo)
        return reverse_lazy('user_profile', kwargs={'username': user})


def altriuserProfileView(request, username, ):
    '''
    Visualizza profilo utente esterno
    :param username: nome utente esterno da visualizzare
    '''
    user = get_object_or_404(User, username=username)
    articoli_utente = Articolo.objects.filter(autore_articolo=user.pk).order_by("-pk")
    context = {"user": user, "articoli_utente": articoli_utente}
    return render(request, 'core/user_profile.html', context)


class ArticoloChange(UpdateView):
    '''
    Modifica il titolo dell'articolo
    '''
    model = Articolo
    fields = ('titolo',)
    template_name = 'core/modifica.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Articolo, id=articleid)

        if user.id is not articolo.autore_articolo.id:
            return visualizzaArticolo(request, articleid)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        articleid = self.kwargs['pk']
        articolo = get_object_or_404(Articolo, id=articleid)
        user = get_object_or_404(User, username=articolo.autore_articolo)
        return reverse_lazy('user_profile', kwargs={'username': user})


class ShowBlacklist(DetailView):
    '''
    Mosrtra la blacklist dell'utente
    '''
    model = UserProfile
    template_name = 'core/blacklist.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        profiloid = self.kwargs['pk']
        profilo = get_object_or_404(UserProfile, id=profiloid)

        if user.id is not profilo.user.id:
            return altriuserProfileView(request, user.username)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowBlacklist, self).get_context_data()
        profiloid = self.kwargs['pk']
        profilo = get_object_or_404(UserProfile, id=profiloid)
        context['wordlist'] = profilo.blacklist.keys()
        context['id'] = profiloid

        return context


class UpdateBlacklist(FormView):
    '''
    Modifica la blacklist dell'utente
    '''
    template_name = "core/modifica_blacklist.html"
    form_class = BlacklistForm
    success_url = reverse_lazy('blacklist')

    def get_form_kwargs(self):
        kwargs = super(UpdateBlacklist, self).get_form_kwargs()
        kwargs.update(({'pk': self.kwargs['pk']}))
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UpdateBlacklist, self).get_context_data()
        context['pk'] = self.kwargs['pk']
        return context


    def get_success_url(self):
        profilo = UserProfile.objects.get(id=self.kwargs['pk'])
        success_url = reverse_lazy('blacklist', kwargs={'pk': profilo.id})
        return success_url




def deleteBlacklist(request, pk):
    '''
    Elimina la parola dalla blacklist
    :param pk: id utente
    '''
    if request.method == 'POST':
        profilo = UserProfile.objects.get(id=pk)
        parola = request.POST['parola']
        profilo.deleteWord(parola)

    return JsonResponse({'message': 'OK'})
