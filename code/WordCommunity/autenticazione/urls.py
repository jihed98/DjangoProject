from django.urls import include, path
from autenticazione import views as auth_view
from django.contrib.auth import views as django_auth

app_name = 'autenticazione'

urlpatterns = [
    path('', auth_view.auth_home, name='auth-home'),
    path('register/', auth_view.UserCreateView.as_view(), name='create-user'),
    path('login/', django_auth.LoginView.as_view(), name='login'),
    path('logout/', django_auth.LogoutView.as_view(), name='logout'),

    path('prova/', auth_view.home, name='registration-fake'),
    path('prova2/', auth_view.exit, name='exit-fake'),
]
