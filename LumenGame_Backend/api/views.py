from wsgiref.util import request_uri
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from . import models


def register(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        user_query = models.User.objects.filter(user_id=user_id)
        if user_query.exists():
            return JsonResponse({
                'status': 0,
                'message': '用户名已经存在',
                'data': {}
            }, json_dumps_params={'ensure_ascii': False})
        else:
            models.User.objects.create(user_id=user_id, password=password)
            return JsonResponse({
                'status': 1,
                'message': '注册成功',
                'data': {
                    'user_id': user_id
                }       
            }, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'GET':
        return JsonResponse({
            'status': 0,
            'message': 'GET不到',
            'data': {}
        }, json_dumps_params={'ensure_ascii': False})


def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        user_query = models.User.objects.filter(user_id=user_id, password=password)
        if user_query.exists():
            return JsonResponse({
                'status': 1,
                'message': '登陆成功',
                'data': {
                    'user_id': user_id
                },
            }, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({
                'status': 0,
                'message': '用户名不存在或密码错误'
            }, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'GET':
        return JsonResponse({
            'status': 0,
            'message': 'GET不到',
            'data': {}
        }, json_dumps_params={'ensure_ascii': False})


def change_password(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        user_query = models.User.objects.filter(user_id=user_id, password=password)
        if user_query.exists():
            # TODO 修改数据库密码
            return JsonResponse({
                'status': 1,
                'message': '密码修改成功',
                'data': {
                    'user_id': user_id
                },
            }, json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({
                'status': 0,
                'message': '用户名和密码校验失败'
            }, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'GET':
        return JsonResponse({
            'status': 0,
            'message': 'GET不到',
            'data': {}
        }, json_dumps_params={'ensure_ascii': False})


def recommend_by_user_id(request):
    # TODO GET方法：根据 user_id 获取 推荐游戏 返回值为JSON格式的游戏数据
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        user_id = request.GET['user_id']
        # 下面根据封装好的推荐算法完成接口
        # game_query = models.Game.objects.filter(user_id=user_id)
        # ...
        return JsonResponse({
            'status': 1,
            'message': '推荐成功',
            'data': {
                # 这里放游戏数据（字典格式）
            }
        }, json_dumps_params={'ensure_ascii': False})
        


