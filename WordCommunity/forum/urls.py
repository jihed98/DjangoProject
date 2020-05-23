from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('nuovo-articolo/', login_required(views.CreaArticolo.as_view()), name="crea_articolo"),
    path('articolo/<int:pk>/', login_required(views.visualizzaArticolo), name="articolo_view"),
    path('classifica/', login_required(views.visualizzaClassifica), name="classifica_view"),
    path('articolo/confronta/', login_required(views.scegliArticoliView), name="articolo-scegli"),
    path('articolo/confronta/<pk1>/<pk2>/', login_required(views.confrontaArticoliView), name="articolo-confronta"),

  ]