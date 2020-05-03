from django.contrib import admin
from django.urls import path, include
from news.views import home,articoloDetailView

urlpatterns = [
    
    path('', home, name="homeview"),
    path('articolo/<int:pk>', articoloDetailView , name="articolo_deatil")

]