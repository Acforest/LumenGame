from django.urls import path
from . import views


urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/signin/', views.signin, name='signin'),
    path('user/signout/', views.signout, name='signout'),
    path('user/user_info/', views.user_info, name='user_info'),
    path('banner/get_banner/', views.get_banner, name='get_banner'),
    path('game/get_game/', views.get_game, name='get_game'),
    path('game/get_rank/', views.get_rank, name='get_rank'),
    path('game/get_rec_game1/', views.get_rec_game1, name='get_rec_game1'),
    path('game/get_rec_game2/', views.get_rec_game2, name='get_rec_game2'),
    path('game/get_search_game/', views.get_search_game, name='get_search_game'),
    path('game/get_search_tag/', views.get_search_tag, name='get_search_tag'),
    path('repository/get_repository_game/', views.get_repository_game, name='get_repository_game'),
    # path('bulk/', views.bulk, name='bulk'),
]