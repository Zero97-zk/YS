import datetime
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
from tools.token_check import logging_check, KEY
from todo.models import DayTodo, WeekTodo, MonthTodo, YearTodo
from user.models import User


# error code --> 105..

# def test(request):
#     return HttpResponse('<h1>OK</h1>')


@logging_check('GET')
def get_index_todos(request):
    if request.method != 'GET':
        return JsonResponse({'code': 10528, 'error': 'Method is wrong!'})
    user = request.user
    now = datetime.datetime.now()
    year, month, week, day = now.year, now.month, now.isocalendar()[1], now.timetuple()[7]
    year_todos = YearTodo.objects.filter(user_id=user.id, year=year)
    year_todos = [{
        "todo_id": todo.id,
        "content": todo.content,
        "level": todo.level,
        "state": todo.state
    } for todo in year_todos]
    month_todos = MonthTodo.objects.filter(user_id=user.id, year=year, month=month)
    month_todos = [{
        "todo_id": todo.id,
        "content": todo.content,
        "level": todo.level,
        "state": todo.state
    } for todo in month_todos]
    week_todos = WeekTodo.objects.filter(user_id=user.id, year=year, week=week)
    week_todos = [{
        "todo_id": todo.id,
        "content": todo.content,
        "level": todo.level,
        "state": todo.state
    } for todo in week_todos]
    day_todos = DayTodo.objects.filter(user_id=user.id, year=year, day=day)
    day_todos = [{
        "todo_id": todo.id,
        "content": todo.content,
        "level": todo.level,
        "state": todo.state
    } for todo in day_todos]
    return JsonResponse({
        'code':200,
        'day': day_todos,
        'week': week_todos,
        'month': month_todos,
        'year': year_todos
    })


@logging_check('GET', 'POST', 'PUT', 'DELETE')
def day_todos(request, year=None, day=None):
    user = request.user
    if request.method == 'GET':
        day = int(day) if day else None
        year = int(year) if year else None
        if not day or not year:
            return JsonResponse({'code': 10501, 'error': 'Not data!'})
        u_id = user.id
        todos = DayTodo.objects.filter(user_id=u_id, year=year,day=day)
        data = [{
            "todo_id": todo.id,
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
        # json --> {'todo_id', 'content', 'level', 'state}
        user = request.user
        query_put = request.body
        put_data = json.loads(query_put)
        if not put_data or not put_data.get('todo_id'):
            return JsonResponse({'code':10504, 'error': 'Not data!'})
        todo_id = put_data.get('todo_id')
        u_id = user.id
        put_dict = {}
        if put_data.get('content'):
            put_dict['content'] = put_data.get('content')
        if put_data.get('level'):
            put_dict['level'] = put_data.get('level')
        if put_data.get('state'):
            put_dict['state'] = put_data.get('state')
        try:
            DayTodo.objects.filter(user_id=u_id, id=todo_id).update(**put_dict)
        except Exception as e:
            return JsonResponse({'code': 10505, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'DELETE':
        # json --> {'todo_id'}
        user = request.user
        query_delete = request.body
        delete_data = json.loads(query_delete)
        if not delete_data or not delete_data.get('todo_id'):
            return JsonResponse({'code': 10506, 'error': 'Not data!'})
        todo_id = delete_data.get('todo_id')
        try:
            DayTodo.objects.get(user_id = user.id, id=todo_id).delete()
        except Exception as e:
            return JsonResponse({'code': 10507, 'error': str(e)})
        return JsonResponse({'code': 200})


@logging_check('GET', 'POST', 'PUT', 'DELETE')
def week_todos(request, year=None, week=None):
    user = request.user
    if request.method == 'GET':
        week = int(week) if week else None
        year = int(year) if year else None
        if not week or not year:
            return JsonResponse({'code': 10508, 'error': 'Not data!'})
        u_id = user.id
        todos = WeekTodo.objects.filter(user_id=u_id, year=year, week=week)
        data = [{
            "todo_id": todo.id,
            "content": todo.content,
            "level": todo.level,
            "state": todo.state
        } for todo in todos]
        return JsonResponse({'code': 200, 'data': data})
    elif request.method == 'POST':
        # json --> {'content', 'year', 'week', 'level'}
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data:
            return JsonResponse({'code': 10509, 'error': 'Not data!'})
        u_id = user.id
        year = post_data.get('year')
        content = post_data.get('content')
        week = post_data.get('week')
        level = post_data.get('level')
        try:
            WeekTodo.objects.create(user_id=u_id, content=content, year=year, week=week, level=level)
        except Exception as e:
            return JsonResponse({'code': 10510, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'PUT':
        # json --> {'todo_id', 'content', 'level', 'state}
        user = request.user
        query_put = request.body
        put_data = json.loads(query_put)
        if not put_data or not put_data.get('todo_id'):
            return JsonResponse({'code': 10511, 'error': 'Not data!'})
        todo_id = put_data.get('todo_id')
        u_id = user.id
        put_dict = {}
        if put_data.get('content'):
            put_dict['content'] = put_data.get('content')
        if put_data.get('level'):
            put_dict['level'] = put_data.get('level')
        if put_data.get('state'):
            put_dict['state'] = put_data.get('state')
        try:
            WeekTodo.objects.filter(user_id=u_id, id=todo_id).update(**put_dict)
        except Exception as e:
            return JsonResponse({'code': 10511, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'DELETE':
        # json --> {'todo_id'}
        user = request.user
        query_delete = request.body
        delete_data = json.loads(query_delete)
        if not delete_data or not delete_data.get('todo_id'):
            return JsonResponse({'code': 10512, 'error': 'Not data!'})
        todo_id = delete_data.get('todo_id')
        try:
            WeekTodo.objects.get(user_id=user.id, id=todo_id).delete()
        except Exception as e:
            return JsonResponse({'code': 10513, 'error': str(e)})
        return JsonResponse({'code': 200})


@logging_check('GET', 'POST', 'PUT', 'DELETE')
def month_todos(request, year=None, month=None):
    user = request.user
    if request.method == 'GET':
        month = int(month) if month else None
        year = int(year) if year else None
        if not month or not year:
            return JsonResponse({'code': 10514, 'error': 'Not data!'})
        u_id = user.id
        todos = MonthTodo.objects.filter(user_id=u_id, year=year, month=month)
        data = [{
            "todo_id": todo.id,
            "content": todo.content,
            "level": todo.level,
            "state": todo.state
        } for todo in todos]
        return JsonResponse({'code': 200, 'data': data})
    elif request.method == 'POST':
        # json --> {'content', 'year', 'month', 'level'}
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data:
            return JsonResponse({'code': 10515, 'error': 'Not data!'})
        u_id = user.id
        year = post_data.get('year')
        content = post_data.get('content')
        month = post_data.get('month')
        level = post_data.get('level')
        try:
            MonthTodo.objects.create(user_id=u_id, content=content, year=year, month=month, level=level)
        except Exception as e:
            return JsonResponse({'code': 10516, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'PUT':
        # json --> {'todo_id', 'content', 'level', 'state}
        user = request.user
        query_put = request.body
        put_data = json.loads(query_put)
        if not put_data or not put_data.get('todo_id'):
            return JsonResponse({'code': 10517, 'error': 'Not data!'})
        todo_id = put_data.get('todo_id')
        u_id = user.id
        put_dict = {}
        if put_data.get('content'):
            put_dict['content'] = put_data.get('content')
        if put_data.get('level'):
            put_dict['level'] = put_data.get('level')
        if put_data.get('state'):
            put_dict['state'] = put_data.get('state')
        try:
            MonthTodo.objects.filter(user_id=u_id, id=todo_id).update(**put_dict)
        except Exception as e:
            return JsonResponse({'code': 10518, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'DELETE':
        # json --> {'todo_id'}
        user = request.user
        query_delete = request.body
        delete_data = json.loads(query_delete)
        if not delete_data or not delete_data.get('todo_id'):
            return JsonResponse({'code': 10519, 'error': 'Not data!'})
        todo_id = delete_data.get('todo_id')
        try:
            MonthTodo.objects.get(user_id=user.id, id=todo_id).delete()
        except Exception as e:
            return JsonResponse({'code': 10520, 'error': str(e)})
        return JsonResponse({'code': 200})


@logging_check('GET', 'POST', 'PUT', 'DELETE')
def year_todos(request, year=None):
    user = request.user
    if request.method == 'GET':
        year = int(year) if year else None
        if not year:
            return JsonResponse({'code': 10521, 'error': 'Not data!'})
        u_id = user.id
        todos = YearTodo.objects.filter(user_id=u_id, year=year)
        data = [{
            "todo_id": todo.id,
            "content": todo.content,
            "level": todo.level,
            "state": todo.state
        } for todo in todos]
        return JsonResponse({'code': 200, 'data': data})
    elif request.method == 'POST':
        # json --> {'content', 'year', 'level'}
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data:
            return JsonResponse({'code': 10522, 'error': 'Not data!'})
        u_id = user.id
        year = post_data.get('year')
        content = post_data.get('content')
        level = post_data.get('level')
        try:
            YearTodo.objects.create(user_id=u_id, content=content, year=year, level=level)
        except Exception as e:
            return JsonResponse({'code': 10523, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'PUT':
        # json --> {'todo_id', 'content', 'level', 'state}
        user = request.user
        query_put = request.body
        put_data = json.loads(query_put)
        if not put_data or not put_data.get('todo_id'):
            return JsonResponse({'code': 10524, 'error': 'Not data!'})
        todo_id = put_data.get('todo_id')
        u_id = user.id
        put_dict = {}
        if put_data.get('content'):
            put_dict['content'] = put_data.get('content')
        if put_data.get('level'):
            put_dict['level'] = put_data.get('level')
        if put_data.get('state'):
            put_dict['state'] = put_data.get('state')
        try:
            YearTodo.objects.filter(user_id=u_id, id=todo_id).update(**put_dict)
        except Exception as e:
            return JsonResponse({'code': 10525, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'DELETE':
        # json --> {'todo_id'}
        user = request.user
        query_delete = request.body
        delete_data = json.loads(query_delete)
        if not delete_data or not delete_data.get('todo_id'):
            return JsonResponse({'code': 10526, 'error': 'Not data!'})
        todo_id = delete_data.get('todo_id')
        try:
            YearTodo.objects.get(user_id=user.id, id=todo_id).delete()
        except Exception as e:
            return JsonResponse({'code': 10527, 'error': str(e)})
        return JsonResponse({'code': 200})
