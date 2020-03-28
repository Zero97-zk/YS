import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import F
# Create your views here.

from message.models import Message, Reply, MessageLike, ReplyLike
from user.models import User
from topic.models import Topic
from tools.token_check import logging_check, KEY


# error code --> 104..

# def test(request):
#     return HttpResponse('<h1>OK</h1>')

def get_parent_reply(parent_reply):
    if not parent_reply:
        return {}
    return {
        'r_id': parent_reply.id,
        'user': parent_reply.user.nickname,
        'content': parent_reply.content,
        'like_count': parent_reply.like_count,
        'created_time': parent_reply.created_time
    }


def get_replys(replys):
    if not replys:
        return []
    replys_list = []
    for reply in replys:
        replys_list.append({
            'r_id': reply.id,
            'user': reply.user.nickname,
            'content': reply.content,
            'created_time': reply.created_time,
            'like_count': reply.like_count,
            'reply_count': reply.reply_count,
            'parent_reply': get_parent_reply(reply.parent_reply)
        })
    return replys_list


def get_messages_by_t_id(t_id):
    messages = Message.objects.filter(topic_id=t_id).order_by('-created_time')
    data = []
    for message in messages:
        data.append({
            'm_id': message.id,
            'user': message.user.nickname,
            'content': message.content,
            'created_time': message.created_time,
            'like_count': message.like_count,
            'reply_count': message.reply_count,
            'replys': get_replys(message.replys.all())
        })
    return {'code': 10412, 'data': data}


@logging_check('POST', 'DELETE')
def handle_messages(request, t_id=None):
    if request.method == 'GET':
        # http://127.0.0.1:8000/api/v1/messages/t_id/<t_id>
        if not t_id:
            return JsonResponse({'code': 10401, 'error': 'No topic_id!'})
        t_id = int(t_id)
        res = get_messages_by_t_id(t_id)
        return JsonResponse(res)

    elif request.method == 'POST':
        # json -->  {"t_id","content"}
        user = request.user
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data or not post_data.get('t_id'):
            return JsonResponse({'code': 10401, 'error': 'No topic_id!'})
        t_id = post_data.get('t_id')
        content = post_data.get('content')
        u_id = user.id
        try:
            Message.objects.create(topic_id=t_id, user_id=u_id, content=content)
        except Exception as e:
            return JsonResponse({'code': 10402, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'DELETE':
        # json -->  {"m_id","u_id"->author_id}
        user = request.user
        query_delete = request.body
        delete_data = json.loads(query_delete)
        if not delete_data:
            return JsonResponse({'code': 10403, 'error': 'No data!'})
        m_id = delete_data.get('m_id')
        u_id = delete_data.get('u_id')
        if not m_id or not u_id or u_id != user.id:
            return JsonResponse({'code': 10404, 'error': 'Delete failed!'})
        try:
            Message.objects.get(id=m_id).delete()
        except Exception as e:
            return JsonResponse({'code': 10405, 'error': str(e)})
        return JsonResponse({'code': 200})


@logging_check('POST', 'DELETE')
def handle_replys(request):
    if request.method == 'POST':
        # json -->{'message_id','content','is_second_reply','parent_reply_id'}
        user = request.user
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data:
            return JsonResponse({'code':10406, 'error': 'No data!'})
        content = post_data.get('content')
        m_id = post_data.get('message_id')
        u_id = user.id
        is_second_reply = post_data.get('is_second_reply')
        parent_reply_id = post_data.get('parent_reply_id')
        if is_second_reply:
            if not parent_reply_id:
                return JsonResponse({'code': 10407, 'error': 'No data!'})
            try:
                reply = Reply.objects.filter(id=parent_reply_id)
                reply.update(reply_count=F('reply_count')+1)
            except Exception as e:
                return JsonResponse({'code': 10408, 'error':str(e)})
            try:
                Reply.objects.create(message_id=m_id, user_id=u_id, content=content,is_second_reply=True, parent_reply_id=parent_reply_id)
            except Exception as e:
                return JsonResponse({'code':10409, 'error': str(e)})
        else:
            try:
                Reply.objects.create(message_id=m_id, user_id=u_id, content=content)
            except Exception as e:
                return JsonResponse({'code': 10410, 'error': str(e)})
        try:
            Message.objects.filter(id=m_id).update(reply_count=F('reply_count')+1)
        except Exception as e:
            return JsonResponse({'code': 10411, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'DELETE':
        pass





