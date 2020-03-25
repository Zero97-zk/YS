from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from user.models import User

def topics(request, t_id = None):
    if request.method == 'GET':
        return JsonResponse({'code':200})
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass