import hashlib
import json
import time

import jwt
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
# error code -->103..
from user.models import User


KEY = 'lht'
def ytoken(request):
    if request.method != 'POST':
        res = {'code': 10301, 'error': 'Method is wrong!'}
        return JsonResponse(res)
    js_str = request.body
    if not js_str:
        res = {'code': 10302, 'error': 'Data is null!'}
        return JsonResponse(res)
    js_obj = json.loads(js_str)
    username = js_obj.get('username')
    password = js_obj.get('password')
    avoid_login = js_obj.get('avoid_login')
    print(avoid_login)
    if not username or not password:
        res =  {'code': 10303, 'error': 'Data must complete!'}
        return JsonResponse(res)
    try:
        user = User.objects.get(username=username)
    except Exception as e:
        res = {'code': 10304, 'error': str(e)}
        return JsonResponse(res)
    p_m = hashlib.md5()
    p_m.update(password.encode())
    login_time = str(int(time.time()))
    if p_m.hexdigest() != user.password:
        res = {'code': 10305, 'error': 'Passwd is wrong!'}
        return JsonResponse(res)

    now = time.time()
    payload = {'id': user.id, 'login_time': login_time, 'exp': now+3600*24}
    token = jwt.encode(payload, KEY)
    user.login_time = login_time
    user.avoid_login = avoid_login
    try:
        user.save()
    except Exception as e:
        res = {'code': 10306, 'error':e}
        return JsonResponse(res)
    res = {'code': 200, 'id': user.id, 'token':token.decode()}
    return JsonResponse(res)
