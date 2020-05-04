from django.urls import include, path
from articolo import views as art_view


app_name = 'articolo'

urlpatterns = [
    # path('', auth_view.auth_home, name='auth-home'),
    path('create/', art_view.ArticleFormInsert.as_view(), name='create-article'),
    path('detail/', art_view.detail, name='detail-article')

]
