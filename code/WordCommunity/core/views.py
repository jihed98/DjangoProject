from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from forum.models import Articolo

# Create your views here.
#def homepage(request):
 #   return render(request, 'core/homepage.html')
   
class HomeView(ListView):
    queryset = Articolo.objects.all()
    template_name = 'core/homepage.html'
    context_object_name ="lista_articoli"


def userProfileView(request, username, ):
    user = get_object_or_404(User, username=username)
    articoli_utente = Articolo.objects.filter(autore_articolo=user.pk).order_by("-pk")
    context = {"user":user, "articoli_utente":articoli_utente}
    return render(request, 'core/user_profile.html', context)


class UserList(ListView):
    model = User
    template_name = 'core/users.html'
