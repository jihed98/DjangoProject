from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name='homepage'),
    path('users/', login_required(views.UserList.as_view()), name='user_list'),
    path('user/<username>/', login_required(views.userProfileView), name='user_profile'),
    path('cerca/', login_required(views.cerca), name='cerca'),
   
]