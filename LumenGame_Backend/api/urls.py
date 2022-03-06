from django.urls import path
from . import views


urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/signin/', views.signin, name='signin'),
    path('user/signout/', views.signout, name='signout'),
    path('user/user_info/', views.user_info, name='user_info'),
    path('banner/get_banner/', views.get_banner, name='get_banner'),
    # TODO
    path('game/recommend_by_user_id', views.recommend_by_user_id, name='recommend_by_user_id'),
    # ...
]