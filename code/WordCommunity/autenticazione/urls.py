
from django.urls import include,path
from autenticazione import views as auth_view

app_name = 'autenticazione'
urlpatterns = [
    path('register/', auth_view.UserCreateView.as_view(), name='create-user'),

]