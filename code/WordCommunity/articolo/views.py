from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, CreateView
from articolo.forms import ArticleCrispyForm
from articolo.models import Articolo


class ArticleFormInsert(LoginRequiredMixin, CreateView):
    model = Articolo
    template_name = 'articolo/InsertArticle.html'
    form_class = ArticleCrispyForm
    success_url = reverse_lazy('articolo:detail-article')

    def form_valid(self, form):
        author = form.instance.author
        author.user = self.request.user
        return super().form_valid(form)


class ArticleDetail(DetailView):
    model = Articolo
    template_name = 'articolo/articleDetail.html'
