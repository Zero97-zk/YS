import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
from tools.token_check import logging_check, KEY
from todo.models import DayTodo
from user.models import User


# error code --> 105..

def test(request):
    return HttpResponse('<h1>OK</h1>')


# def get_index_todos(request):
#     pass


@logging_check('GET', 'POST', 'PUT', 'DELETE')
def day_todos(request, day=None):
    day = int(day) if day else None
    user = request.user
    if request.method == 'GET':
        if not day:
            return JsonResponse({'code': 10501, 'error': 'Not day!'})
        u_id = user.id
        todos = DayTodo.objects.filter(user_id=u_id, day=day)
        data = [{
            "content": todo.content,
            "level": todo.level,
            "state": todo.state
        } for todo in todos]
        return JsonResponse({'code': 200, 'data': data})
    elif request.method == 'POST':
        # json --> {'content', 'year', 'day', 'level'}
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data:
            return JsonResponse({'code': 10502, 'error': 'Not data!'})
        u_id = user.id
        year = post_data.get('year')
        content = post_data.get('content')
        day = post_data.get('day')
        level = post_data.get('level')
        try:
            DayTodo.objects.create(user_id=u_id, content=content, year=year, day=day, level=level)
        except Exception as e:
            return JsonResponse({'code': 10503, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'PUT':
        pass



# def week_todos(request, week=None):
#     pass
#
#
# def month_todos(request, month=None):
#     pass
#
#
# def year_todos(request, year=None):
#     pass
