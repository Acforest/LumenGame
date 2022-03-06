from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from . import models
from .utils import json_response


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']
        qq = request.POST['qq']
        user_query = User.objects.filter(username=username)
        if user_query.exists():
            return json_response(0, '用户名已经存在', {})
        else:
            user = User(username=username)
            user.set_password(password)
            user.save()
            models.Player.objects.create(user=user, photo="https://img2.baidu.com/it/u=2161949891,656888789&fm=26&fmt=auto",
                                         phone=phone, email=email, qq=qq)
            return json_response(1, '注册成功', {'username': username})
    elif request.method == 'GET':
        return json_response(0, 'GET不到', {})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            player = models.Player.objects.get(user=user)
            return json_response(1, '登陆成功', 
                                {'id': user.id, 'username': username, 'photo': player.photo,
                                 'phone': player.phone, 'email': player.email, 'qq': player.qq})
        else:
            return json_response(0, '用户名不存在或密码错误', {})
    elif request.method == 'GET':
        return json_response(0, 'GET不到', {})


def signout(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            logout(request)
            return json_response(1, '退出成功', {})
        else:
            return json_response(1, '用户未登录', {})
    elif request.method == 'GET':
        return json_response(0, 'GET不到', {})


def user_info(request):
    if request.method == 'GET':  # 获取用户信息
        pass
        # player = models.Player.objects.get(user=user)
        # return json_response(1, '获取用户信息成功', {
        #     'username': player.user.username,
        #     'photo': player.photo,
        #     'phone': player.phone,
        #     'email': player.email,
        #     'qq': player.qq,
        # })
    elif request.method == 'POST':  # 修改用户密码
        username = request.POST['username']
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        user = authenticate(username=username, password=old_password)
        if user:
            user.set_password(new_password)
            user.save()
            return json_response(1, '修改用户密码成功', {})
        else:
            return json_response(0, '原密码错误', {})
    elif request.method == 'PUT':  # 修改用户信息
        username = request.POST['username']
        photo = request.POST['photo']
        phone = request.POST['phone']
        email = request.POST['email']
        user_query = User.objects.filter(username=username)
        if user_query.exists():
            return json_response(0, '用户名已经存在', {})
        else:
            models.Player.objects.filter(username=username).update(
                username=username, photo=photo,
                phone=phone, email=email
            )
        return json_response(1, '修改用户信息成功', {})



def change_password(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        user_qs = User.objects.filter(user_id=user_id, password=password)
        if user_qs.exists():
            # TODO 修改数据库密码
            return json_response(1, '密码修改成功', {'user_id': user_id})
        else:
            return json_response(0, '用户名和密码校验失败', {})
    elif request.method == 'GET':
        return json_response(0, 'GET不到', {})


def get_banner(request):
    if request.method == 'GET':
        page = request.GET['page']
        size = request.GET['size']
        banner_query = models.Banner.objects.all()[:int(size)]
        banner_json = serializers.serialize('json', banner_query)
        return json_response(1, '获取banner成功', banner_json)
            


def recommend_by_user_id(request):
    # TODO GET方法：根据 user_id 获取 推荐游戏 返回值为JSON格式的游戏数据
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        user_id = request.GET['user_id']
        # 下面根据封装好的推荐算法完成接口
        # game_query = models.Game.objects.filter(user_id=user_id)
        # ...
        return json_response(1, '推荐成功', {}) # 这里放游戏数据（字典格式）
        


