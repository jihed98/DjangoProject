from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name='homepage'),
    path('users/', login_required(views.UserList.as_view()), name='user_list'),
    path('user/<username>/', login_required(views.userProfileView), name='user_profile'),
    path('cerca/', login_required(views.cerca), name='cerca'),
    path('articolo/<int:pk>/delete/', login_required(views.ArticleDelete.as_view()),  name='articolo-delete'),
    path('altriuser/<username>/', login_required(views.altriuserProfileView),  name='altriuser-profile'),
    path('articolo/<int:pk>/modifica/', login_required(views.ArticoloChange.as_view()), name="articolo-modifica"),
    path('user/<int:pk>/blacklist/', login_required(views.ShowBlacklist.as_view()), name="blacklist"),
    path('user/<int:pk>/blacklist/modifica', login_required(views.UpdateBlacklist.as_view()), name="blacklist-modifica"),
    path('user/<int:pk>/blacklist/delete/', login_required(views.deleteBlacklist), name="blacklist-rimuovi"),
]