from django.urls import path
from . import views


urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/signin/', views.signin, name='signin'),
    path('user/signout/', views.signout, name='signout'),
    path('user/user_info/', views.user_info, name='user_info'),
    path('banner/get_banner/', views.get_banner, name='get_banner'),
    # path('game/get_game/', views.get_game, name='get_game'),
    path('game/get_rank/', views.get_rank, name='get_rank'),
    path('game/get_rec_game/', views.get_rec_game, name='get_rec_game1'),
    path('game/get_search_game/', views.get_search_game, name='get_search_game'),
    path('game/get_search_tag/', views.get_search_tag, name='get_search_tag'),
    path('game/like_game/', views.like_game, name='like_game'),
    path('game/cancel_like_game/', views.cancel_like_game, name='cancel_like_game'),
    path('game/get_game_detail/', views.get_game_detail, name='get_game_detail'),
    path('repository/get_repository_game/', views.get_repository_game, name='get_repository_game'),
    path('repository/search_repository_game/', views.search_repository_game, name='search_repository_game'),
    path('repository/search_repository_tag/', views.search_repository_tag, name='search_repository_tag'),
    # path('bulk/', views.bulk, name='bulk'),
]