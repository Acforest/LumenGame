from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
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


def get_banner(request):
    if request.method == 'GET':
        size = request.GET['size']
        banner_query = models.Banner.objects.all()[:int(size)]
        banner_json = serializers.serialize('json', banner_query)
        return json_response(1, '获取banner成功', banner_json)


# def get_game(request):
#     def open_url(url):
#         req = urllib.request.Request(url) # 将Request类实例化并传入url为初始值，然后赋值给req
#         # 添加header，伪装成浏览器
#         req.add_header('User-Agent',
#         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
#         # 访问url，并将页面的二进制数据赋值给page
#         page = urllib.request.urlopen(req)
#         # 将page中的内容转换为utf-8编码
#         html = page.read().decode('utf-8')
#         return html

#     def get_img(html):
#         # [^"]+\.jpg 匹配除"以外的所有字符多次,后面跟上转义的.和png
#         p = r'<img class="game_header_image_full" src="(.*?)">'
#         # 返回正则表达式在字符串中所有匹配结果的列表
#         imglist = re.findall(p, html)
#         return imglist[0] if imglist else ''

#     if request.method == 'GET':
#         game_query = models.GameInfo.objects.all()[:50]
#         # for item in game_query:
#         #     item.url = get_img(open_url(item.url))
#         game_json = serializers.serialize('json', game_query)
#         return json_response(1, '获取game成功', game_json)


def get_game_detail(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        game_name = request.GET['game_name']
        game_detail_query = models.GameInfo.objects.filter(name=game_name)
        like_query = models.Repository.objects.filter(user_id=user_id, game_name=game_name)
        like = like_query.exists()
        game_detail_json = serializers.serialize('json', game_detail_query)
        return JsonResponse({
            'status': 1,
            'message': '获取推荐成功',
            'like': like,
            'detail': game_detail_json,
        }, json_dumps_params={'ensure_ascii': False})


def get_rank(request):
    if request.method == 'GET':
        rank_query = models.GameRank.objects.all()
        rank_json = serializers.serialize('json', rank_query)
        return json_response(1, '获取rank成功', rank_json)


def get_rec_game(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        rec_query_1 = models.GameInfo.objects.raw(
            'SELECT game_info.* FROM game_info, recommend_1 WHERE game_info.name = recommend_1.name AND recommend_1.user_id = %s',
            [user_id]
        )
        rec_query_2 = models.GameInfo.objects.raw(
            'SELECT game_info.* FROM game_info, recommend_2 WHERE game_info.name = recommend_2.name AND recommend_2.user_id = %s',
            [user_id]
        )
        rec_query_3 = models.GameInfo.objects.all().order_by('?')[:20]
        rec_json_1 = serializers.serialize('json', rec_query_1)
        rec_json_2 = serializers.serialize('json', rec_query_2)
        rec_json_3 = serializers.serialize('json', rec_query_3)
        return JsonResponse({
            'status': 1,
            'message': '获取推荐成功',
            'rec1': rec_json_1,
            'rec2': rec_json_2,
            'rec3': rec_json_3,
        }, json_dumps_params={'ensure_ascii': False})


def get_search_game(request):
    if request.method == 'GET':
        keyword = request.GET['keyword']
        user_id = request.GET['user_id']
        search_query = models.GameInfo.objects.filter(name__icontains=keyword)[:200]
        search_json = serializers.serialize('json', search_query)
        like_query = models.Repository.objects.filter(user_id=user_id)
        like_json = serializers.serialize('json', like_query)
        return JsonResponse({
            'status': 1,
            'message': '获取搜索成功',
            'search_json': search_json,
            'like_json': like_json
        }, json_dumps_params={'ensure_ascii': False})


def get_search_tag(request):
    if request.method == 'GET':
        keyword = request.GET['tag']
        search_query = models.GameInfo.objects.filter(popular_tags__icontains=keyword).order_by('?')[:20]
        search_json = serializers.serialize('json', search_query)
        return json_response(1, '获取搜索成功', search_json)


def get_repository_game(request):
    if request.method == 'GET':
        user_id = request.GET['user_id']
        repository_query = models.GameInfo.objects.raw(
            'SELECT game_info.* FROM game_info, repository WHERE game_info.name = repository.game_name AND repository.user_id = %s',
            [user_id]
        )
        repository_json = serializers.serialize('json', repository_query)
        return json_response(1, '获取游戏库成功', repository_json)


def search_repository_game(request):
    if request.method == 'GET':
        keyword = request.GET['keyword']
        user_id = request.GET['user_id']
        repository_query = models.GameInfo.objects.raw(
            'SELECT game_info.* FROM game_info, repository WHERE game_info.name = repository.game_name AND repository.user_id = %s AND LOCATE(%s, game_info.name) > 0',
            [user_id, keyword]
        )
        repository_json = serializers.serialize('json', repository_query)
        return json_response(1, '获取游戏库成功', repository_json)


def search_repository_tag(request):
    if request.method == 'GET':
        tag = request.GET['tag']
        user_id = request.GET['user_id']
        repository_query = models.GameInfo.objects.raw(
            'SELECT game_info.* FROM game_info, repository WHERE game_info.name = repository.game_name AND repository.user_id = %s AND LOCATE(%s, game_info.popular_tags) > 0',
            [user_id, tag]
        )
        repository_json = serializers.serialize('json', repository_query)
        return json_response(1, '获取游戏库成功', repository_json)


def like_game(request):
    if request.method == 'POST':
        try:
            user_id = request.POST['user_id']
            game_name = request.POST['game_name']
            models.Repository.objects.create(user_id=user_id, game_name=game_name,
                                            hours=0, purchase=0, play=0)
            return json_response(1, '喜欢游戏成功', {})
        except:
            return json_response(0, '喜欢游戏失败', {})

def cancel_like_game(request):
    if request.method == 'POST':
        try:
            user_id = request.POST['user_id']
            game_name = request.POST['game_name']
            models.Repository.objects.filter(user_id=user_id, game_name=game_name).delete()
            return json_response(1, '取消喜欢游戏成功', {})
        except:
            return json_response(0, '取消喜欢游戏失败', {})


# def bulk(request):
#     from django.contrib.auth.hashers import make_password
#     if request.method == 'GET':
#         module_dir = os.path.dirname(__file__)
#         dir = os.path.join(module_dir, 'user.csv')
#         with open(dir) as f:
#             User.objects.bulk_create([
#                 User(
#                     id=idx,
#                     username=f'test_{idx}',
#                     password=make_password('123456'),
#                     is_active=True,
#                 ) for idx in f.read().splitlines()
#             ])
#         return json_response(1, '导入成功', {})
#     else:
#         return json_response(0, '导入失败', {})