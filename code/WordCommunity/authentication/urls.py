
from django.urls import include,path
from authentication import views as auth_view

app_name = 'authentication'
urlpatterns = [
    path('register/', auth_view.UserCreateView.as_view(), name='create-user'),

]