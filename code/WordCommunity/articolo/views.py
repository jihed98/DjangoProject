from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, CreateView
from articolo.forms import ArticleCrispyForm
from articolo.models import Articolo


class ArticleFormInsert(CreateView):
    model = Articolo
    template_name = 'articolo/InsertArticle.html'
    form_class = ArticleCrispyForm
    success_url = reverse_lazy('articolo:detail-article')

    '''
    TRAMITE QUESTO BECCO LO USER SU FORM NELL'INIT
    '''
    def get_form_kwargs(self):
        kwargs = super(ArticleFormInsert, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ArticleDetail(DetailView):
    model = Articolo
    template_name = 'articolo/articleDetail.html'

''' USO QUESTO SENZA IL PK PERCHÈ MI DAVA PROBLEMI'''
def detail (request):
    return render(request, 'articolo/articleDetail.html')
