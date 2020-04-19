import time
import jwt
from django.http import JsonResponse
from user.models import User

# error code --> 102..

KEY = 'lht'

def logging_check(*method):
    def _logging_check(func):
        def wrapper(request, *args, **kwargs):
            token = request.META.get('HTTP_AUTHORIZATION')
            if not method:
                return func(request, *args, **kwargs)
            if request.method not in method:
                return func(request, *args, **kwargs)
            if not token:
                res = {'code': 10201, 'error': 'Plase logging!!'}
                return JsonResponse(res)
            try:
                token = jwt.decode(token, KEY)
            except Exception as e:
                res = {'code':10202, 'error':"Token don't match!"}
                return JsonResponse(res)
            id = token.get('id')
            login_time = token.get('login_time')
            try:
                user = User.objects.get(id=id)
            except Exception as e:
                print(e)
                res = {'code':10203, 'error':'Not found user!'}
                return JsonResponse(res)
            if login_time != user.login_time:
                res = {'code': 10202, 'error':'Please login again!'}
                return JsonResponse(res)
            request.user = user
            return func(request, *args, **kwargs)
        return wrapper
    return _logging_check

def get_user(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        res = jwt.decode(token, KEY)
    except Exception as e:
        return None
    u_id = res.get('id')
    try:
        user = User.objects.get(id=u_id)
    except Exception as e:
        return None
    return user
