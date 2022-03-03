from django.urls import path
from . import views


urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/signin/', views.signin, name='signin'),
    path('user/signout/', views.signout, name='signout'),
    # TODO
    # path('user/change_password/', views.change_password, name='change_password'),
    path('game/recommend_by_user_id', views.recommend_by_user_id, name='recommend_by_user_id'),
    # ...
]