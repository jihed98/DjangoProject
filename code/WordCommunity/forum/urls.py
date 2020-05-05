from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('nuovo-articolo/', login_required(views.CreaArticolo.as_view()), name="crea_articolo"),
   path('articolo/<int:pk>/', login_required(views.visualizzaArticolo), name="articolo_view"),
  ]