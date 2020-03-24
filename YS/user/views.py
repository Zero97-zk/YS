import hashlib
import json
import time
import jwt
import os
import platform
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from user.models import User
from tools.token_check import logging_check, KEY
from YS.settings import BASE_DIR


# Create your views here.

def test(request):
    return HttpResponse('ok')

@logging_check('PUT')
def users(request, id=None):
    if request.method == 'GET':
        user = None
        try:
            user = User.objects.get(id=int(id))
        except Exception as e:
            # print(e)
            pass
        if not user:
            res = {'code': 10001, 'error': 'User does not exist!!'}
            return JsonResponse(res)
        if request.GET.keys():
        # 有查询字符串获取相应数据
            data = {}
            for key in request.GET.keys():
                if key == 'password':
                    continue
                if key == 'avatar':
                    data[key] = str(getattr(user, key))
                    continue
                if hasattr(user,key):
                    data[key] = getattr(user, key)
            res = {'code': 200, 'id':int(id), 'data':data}
            return JsonResponse(res)
        else:
        # 无查询字符串获取用户全量有信息
            res = {'code': 200, 'id':int(id), 'data':{
                'username': user.username,
                'nickname': user.nickname,
                'email': user.email,
                'phone': user.phone,
                'description': user.description,
                'login_time': user.login_time,
                'avatar': str(user.avatar)
            }}
            return JsonResponse(res)

    elif request.method == 'POST':
        # 注册
        js_str = request.body
        # print(js_str)
        if not js_str:
            res = {'code': 10002, 'error': 'Data is null!!'}
            return JsonResponse(res)
        js_obj = json.loads(js_str)
        # print(js_obj)
        username = js_obj.get('username')
        password = js_obj.get('password')
        email = js_obj.get('email')
        phone = js_obj.get('phone')
        if not username or not password or not email or not phone:
            res = {'code':10003, 'error': 'Data is not complete!'}
            return JsonResponse(res)

        # 检查用户名是否可用
        user_exist = True if User.objects.filter(username=username) else False
        if user_exist:
            res = {'code': 10004, 'error': 'Username already exists'}
            return JsonResponse(res)

        p_m = hashlib.md5()
        p_m.update(password.encode())
        login_time = str(int(time.time()))

        # 创建用户
        try:
            user = User.objects.create(username=username, password=p_m.hexdigest(), nickname=username,
                                       email=email, phone=phone, login_time=login_time)
        except Exception as e:
            # print(e)
            res = {'code':10005, 'error': 'regist failed!!'}
            return JsonResponse(res)

        # 生成token
        now = time.time()
        payload = {'id': user.id, 'login_time':login_time, 'exp': now+3600*24}
        token = jwt.encode(payload, KEY)
        res = {'code': 200, 'id': user.id, 'token': token.decode()}
        return JsonResponse(res)

    elif request.method == 'PUT':
        # 更改用户信息
        user = request.user
        if user.id != int(id):
            res = {'code': 10008, 'error': "You can't update other info!"}
        js_str = request.body
        if not js_str:
            res = {'code': 10006, 'error': 'Data is Null!'}
            return JsonResponse(res)
        js_obj = json.loads(js_str)
        for key in js_obj:
            if key == 'password':
                continue
            if hasattr(user, key) and js_obj.get(key):
                setattr(user, key, js_obj.get(key))
        try:
            user.save()
        except Exception as e:
            # print(e)
            res = {'code': 10007, 'error': e}
            return JsonResponse(res)
        res = {'code':200, 'id':int(id)}
        return JsonResponse(res)

@logging_check('POST')
def avatar(request, id):
    # 用户上传头像
    if request.method != 'POST':
        res = {'code':10009, 'error': 'Request method is wrong!!'}
        return JsonResponse(res)

    user = request.user
    if int(id) != user.id:
        res = {'code':10010, 'error': "You can't update other avatar"}
        return JsonResponse(res)
    user_avatar = request.FILES['avatar']
    if not user_avatar:
        res = {'code': 10011, 'error': "Not avatar!"}
        return JsonResponse(res)
    now_time =  str(int(round(time.time()*1000)))
    user_avatar.name = now_time+'.'+user_avatar.name.split('.')[-1]
    # print(platform.system())
    if platform.system() == 'Windows':
        # print(BASE_DIR+'\\'+str(user.avatar).replace('/','\\'))
        if os.path.exists(BASE_DIR+'\\media\\'+str(user.avatar).replace('/','\\')):
            os.remove(BASE_DIR+'\\media\\'+str(user.avatar).replace('/','\\'))
    elif platform.system() == 'Linux':
        if os.path.exists(BASE_DIR+'/media/'+str(user.avatar)):
            os.remove(BASE_DIR+'/media/'+str(user.avatar))
    user.avatar = user_avatar
    try:
        user.save()
    except Exception as e:
        res = {'code': 10011, 'error':e}
        return JsonResponse(res)
    res = {'code': 200, 'id':int(id)}
    return JsonResponse(res)












