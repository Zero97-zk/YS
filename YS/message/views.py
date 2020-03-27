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

@logging_check('POST', 'DELETE')
def handle_messages(request, t_id=None):
    if request.method == 'GET':
        if not t_id:
            return JsonResponse({'code': 10401, 'error': 'No topic_id!'})
        t_id = int(t_id)
        pass

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
        # json -->  {"t_id","u_id"->author_id}
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





