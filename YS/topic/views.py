import datetime
import json
import time

from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from django.db.models import F

from user.models import User
from topic.models import Topic, TopicCollectUser, TopicLikeUser, TopicImage
from tools.token_check import KEY, get_user, logging_check


# Create your views here.
# error code --> 102..


def query_to_dict(query_dict):
    d = {}
    for key in query_dict:
        d[key] = query_dict[key]
    return d


def get_topic_type(query_dict):
    if 'type' in query_dict:
        return query_dict['type']


def rec_obj_to_dict(rec_obj):
    return {
        'id': rec_obj.id,
        'type': rec_obj.type,
        'title': rec_obj.title,
        'introduce': rec_obj.introduce,
        'content': rec_obj.content,
        'message_count': rec_obj.message_count,
        'created_time': str(rec_obj.created_time)[:19],
        'updated_time': rec_obj.updated_time,
        'like_count': rec_obj.like_count,
        'watch_count': rec_obj.watch_count,
        'collect_count': rec_obj.collect_count,
        'author_id': rec_obj.author.id,
        'author_name': rec_obj.author.nickname,
        'author_avatar': str(rec_obj.author.avatar),
        'limit': rec_obj.limit

    } if rec_obj else {}


def get_index_topics(query_dict):
    topic_type = get_topic_type(query_dict)
    hot_topics = []
    try:
        if not topic_type:
            topics = Topic.objects.filter(limit='public').order_by('-created_time')[:100]
            now = datetime.datetime.now()
            start = datetime.datetime(now.year, now.month, 1)
            end = datetime.datetime(now.year, now.month + 1, 1)
            hot_topics = Topic.objects.filter(limit='public', created_time__gt=start, created_time__lt=end).order_by('-watch_count')[:10]
            hot_topics = [rec_obj_to_dict(x) for x in hot_topics]
        else:
            topics = Topic.objects.filter(limit='public', type=topic_type).order_by('-created_time')[:100]
    except Exception as e:
        return {'code': 10201, 'error': str(e)}
    # topics = sorted(topics, key=lambda x: -x.watch_count)
    data = [rec_obj_to_dict(x) for x in topics]
    return {'code': 200, 'data': data, 'hot_topics': hot_topics}


def get_topic_by_t_id(t_id, look_user=None):
    try:
        topic = Topic.objects.get(id=t_id)
    except Exception as e:
        return {'code': 10202, 'error': str(e)}
    if (not look_user or look_user != topic.author) and topic.limit == 'private':
        return {'code': 10203, 'error': 'Not topic!'}
    if look_user == topic.author:
        prev_topic = Topic.objects.filter(id__gt=t_id, author=topic.author).first()
        next_topic = Topic.objects.filter(id__lt=t_id, author=topic.author).last()
    else:
        prev_topic = Topic.objects.filter(id__gt=t_id, author=topic.author, limit='public').first()
        next_topic = Topic.objects.filter(id__lt=t_id, author=topic.author, limit='public').last()
    if prev_topic:
        prev_id = prev_topic.id
        prev_title = prev_topic.title
    else:
        prev_id = None
        prev_title = None
    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    else:
        next_id = None
        next_title = None
    data = rec_obj_to_dict(topic)
    data["next_id"] = next_id
    data["next_title"] = next_title
    data['prev_id'] = prev_id
    data['prev_title'] = prev_title
    return {'code': 200, 'data': data}


def get_tag_data(topics):
    tag_d = {}
    for topic in topics:
        if topic.type not in tag_d:
            tag_d[topic.type] = [rec_obj_to_dict(topic)]
        else:
            tag_d[topic.type].append(rec_obj_to_dict(topic))
    return [{'tag': x, 'data': tag_d[x]} for x in tag_d]


def get_topic_by_u_id(u_id, look_user=None):
    try:
        if not look_user or look_user.id != u_id:
            topics = Topic.objects.filter(author_id=u_id, limit='public').order_by('-created_time')
        else:
            topics = Topic.objects.filter(author_id=u_id).order_by('-created_time')
    except Exception as e:
        return {'code': 10204, 'error': str(e)}
    data = [rec_obj_to_dict(x) for x in topics]
    tag_data = get_tag_data(topics)
    return {'code': 200, 'data': data, 'tag_data': tag_data}

def get_delete_data(request):
    print(list(QueryDict(request.body).keys())[0],type(list(QueryDict(request.body).keys())[0]))
    return list(QueryDict(request.body).keys())[0].get('data')


@logging_check('POST', 'PUT', 'DELETE')
def handle_topics(request, t_id=None, u_id=None):
    t_id = int(t_id) if t_id else None
    u_id = int(u_id) if u_id else None
    if request.method == 'GET':
        look_user = get_user(request)
        query_get = request.GET
        if not t_id and not u_id:
            # 获取主页文章
            res = get_index_topics(query_get)
            return JsonResponse(res)
        elif t_id:
            res = get_topic_by_t_id(t_id, look_user)
            return JsonResponse(res)
        elif u_id:
            res = get_topic_by_u_id(u_id, look_user)
            return JsonResponse(res)

    elif request.method == 'POST':
        user = request.user
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data:
            return JsonResponse({'code': 10205, 'error':'No data!'})
        data = {'author_id': user.id}
        for key in post_data:
            if hasattr(Topic, key):
                data[key] = post_data[key]
        try:
            topic = Topic.objects.create(**data)
        except Exception as e:
            return JsonResponse({'code': 10206, 'error': str(e)})
        return JsonResponse({'code': 200, 'topic_id': topic.id, 'author_id':topic.author.id})

    elif request.method == 'PUT':
        user = request.user
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data:
            return JsonResponse({'code': 10207, 'error': 'Not data!'})
        try:
            topic = Topic.objects.get(id=t_id)
        except Exception as e:
            return JsonResponse({'code': 10208, 'error': str(e)})
        if not topic or topic.author != user:
            return JsonResponse({'code': 10209, 'error': "You can't update other's topic!"})
        for key in post_data:
            if hasattr(Topic, key) and post_data.get(key):
                setattr(topic, key, post_data[key])
        try:
            topic.save()
        except Exception as e:
            return JsonResponse({'code': 10210, 'error': str(e)})
        return JsonResponse({'code': 200, 'data': rec_obj_to_dict(topic)})

    elif request.method == 'DELETE':
        user = request.user
        try:
            topic = Topic.objects.get(id=t_id)
        except Exception as e:
            return JsonResponse({'code': 10211, 'error': str(e)})
        if not topic or topic.author != user:
            return JsonResponse({'code': 10212, 'error': "You can't delete other's topic!"})
        try:
            topic.delete()
        except Exception as e:
            return JsonResponse({'code': 10213, 'error': str(e)})
        return JsonResponse({'code': 200})

def day_topics(request):
    if request.method != 'GET':
        return JsonResponse({'code': 10241, 'error': 'Method is wrong!'})
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    if not year or not month or not day:
        return JsonResponse({'code': 10242, 'error': 'Data is not completed!'})
    topics = Topic.objects.filter(created_time__gt=datetime.datetime(int(year), int(month), int(day)), created_time__lt=datetime.datetime(int(year), int(month), int(day)+1), limit='public').order_by('-watch_count')
    data = [rec_obj_to_dict(x) for x in topics]
    return JsonResponse({'code': 200, 'data': data})

def get_title_topics(request):
    if request.method != 'GET':
        return JsonResponse({'code': 10242, 'error': 'Method is wrong!'})
    title = request.GET.get('title')
    if not title:
        return JsonResponse({'code': 10243, 'error': 'Data is not completed!'})
    topics = Topic.objects.filter(title__contains=title, limit='public').order_by('-watch_count')
    data = [rec_obj_to_dict(x) for x in topics]
    return JsonResponse({'code': 200, 'data': data})

def get_nickname_topics(request):
    if request.method != 'GET':
        return JsonResponse({'code': 10243, 'error': 'Method is wrong!'})
    nickname = request.GET.get('nickname')
    if not nickname:
        return JsonResponse({'code': 10244, 'error': 'Data is not completed!'})
    users = User.objects.filter(nickname=nickname)
    user_ids = [x.id for x in users]
    topics = Topic.objects.filter(author_id__in=user_ids, limit='public').order_by('-watch_count')
    data = [rec_obj_to_dict(x) for x in topics]
    return JsonResponse({'code': 200, 'data': data})

def get_collect_by_uid(u_id, look_user=None):
    try:
        collect_user = User.objects.get(id=u_id)
    except Exception as e:
        return {'code': 10222, 'error': str(e)}
    try:
        if not look_user or look_user.id != u_id:
            topics = collect_user.collect_topics.filter(limit='public')
        else:
            topics = collect_user.collect_topics.all()
    except Exception as e:
        return {'code': 10217, 'error': str(e)}
    data = [rec_obj_to_dict(x) for x in topics]
    collected_topic_ids = [x.id for x in topics]
    return{'code': 200, 'data': data, 'topic_ids': collected_topic_ids}


@logging_check('POST', 'DELETE')
def collect_topics(request, u_id=None, t_id=None):
    u_id = int(u_id) if u_id else None
    t_id = int(t_id) if t_id else None
    if request.method == 'GET':
        if not u_id:
            return JsonResponse({'code': 10214, 'error': 'No data!'})
        look_user = get_user(request)
        # 查看某人收藏的文章
        res = get_collect_by_uid(u_id, look_user)
        return JsonResponse(res)
    elif request.method == 'POST':
        user = request.user
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data or not post_data.get('t_id'):
            return JsonResponse({'code': 10215, 'error': 'No data!'})
        t_id = post_data.get('t_id')
        collection = TopicCollectUser.objects.filter(user_id=user.id, topic_id = t_id)
        if collection:
            return JsonResponse({'code':10223, 'error': 'You already collected!'})
        try:
            TopicCollectUser.objects.create(user_id=user.id, topic_id=t_id)
        except Exception as e:
            return JsonResponse({'code': 10216, 'error': str(e)})
        try:
            Topic.objects.filter(id=t_id).update(collect_count=F('collect_count')+1)
        except Exception as e:
            return JsonResponse({'code': 10224, 'error': str(e)})
        return JsonResponse({'code': 200})
    elif request.method == 'DELETE':
        user = request.user
        if not user:
            return JsonResponse({'code': 10218, 'error': 'No data!'})
        if not t_id:
            return JsonResponse({'code': 10219, 'error': 'No data!'})
        try:
            collection = TopicCollectUser.objects.get(user_id=user.id, topic_id=t_id)
        except Exception as e:
            return JsonResponse({'code': 10220, 'error': str(e)})
        try:
            collection.delete()
        except Exception as e:
            return JsonResponse({'code': 10221, 'error': str(e)})
        try:
            Topic.objects.filter(id=t_id).update(collect_count=F('collect_count')-1)
        except Exception as e:
            return JsonResponse({'code': 10225, 'error': str(e)})
        return JsonResponse({'code': 200})

@logging_check('POST', 'DELETE')
def like_topics(request, t_id=None):
    t_id = int(t_id) if t_id else None
    if request.method == 'GET':
        likes = TopicLikeUser.objects.filter(topic_id=t_id)
        return JsonResponse({'code': 200, 'data': [x.user.id for x in likes]})
    elif request.method == 'POST':
        user = request.user
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data or not post_data.get('t_id'):
            return JsonResponse({'code': 10222, 'error': 'No data!'})
        t_id = post_data.get('t_id')
        like = TopicLikeUser.objects.filter(user_id=user.id, topic_id = t_id)
        if like:
            return JsonResponse({'code': 10226, 'error': 'You already Liked!'})
        try:
            TopicLikeUser.objects.create(user_id=user.id, topic_id=t_id)
        except Exception as e:
            return JsonResponse({'code': 10227, 'error': str(e)})
        try:
            Topic.objects.filter(id=t_id).update(like_count=F('collect_count')+1)
        except Exception as e:
            return JsonResponse({'code': 10228, 'error': str(e)})
        return JsonResponse({'code': 200})

    elif request.method == 'DELETE':
        user = request.user
        if not user:
            return JsonResponse({'code': 10229, 'error': 'No data!'})
        if not t_id:
            return JsonResponse({'code': 10230, 'error': 'No data!'})
        try:
            like = TopicLikeUser.objects.get(user_id=user.id, topic_id=t_id)
        except Exception as e:
            return JsonResponse({'code': 10231, 'error': str(e)})
        try:
            like.delete()
        except Exception as e:
            return JsonResponse({'code': 10232, 'error': str(e)})
        try:
            Topic.objects.filter(id=t_id).update(like_count=F('like_count') - 1)
        except Exception as e:
            return JsonResponse({'code': 10233, 'error': str(e)})
        return JsonResponse({'code': 200})

def watch_topics(request):
    if request.method != 'POST':
        return JsonResponse({'code': 10234, 'error': 'The method is wrong!'})
    else:
        query_post = request.body
        post_data = json.loads(query_post)
        if not post_data or not post_data.get('t_id'):
            return JsonResponse({'code': 10235, 'error': 'No data!'})
        t_id = post_data.get('t_id')
        try:
            Topic.objects.filter(id=t_id).update(watch_count=F('watch_count')+1)
        except Exception as e:
            return JsonResponse({'code': 10236, 'error': str(e)})
        return JsonResponse({'code': 200})

@logging_check('POST', 'DELETE')
def topic_image(request):
    user = request.user
    if request.method == 'POST':
        topic_image = request.FILES['topic_image']
        if not topic_image:
            return JsonResponse({'code': 10237, 'error': 'Not image'})
        now_time = str(int(round(time.time() * 1000)))
        topic_image.name = now_time + '.' + topic_image.name.split('.')[-1]
        try:
            img = TopicImage.objects.create(topic_image=topic_image, user=user)
        except Exception as e:
            return JsonResponse({'code': 10238, 'error': str(e)})
        return JsonResponse({'code': 200, 'img_url': 'topicimages/'+topic_image.name, 'img_id': img.id})
    if request.method == 'DELETE':
        query_delete = request.body
        delete_data = json.loads(query_delete)
        img_id = delete_data.get('img_id')
        if not img_id:
            return JsonResponse({'code': 10239, 'error': 'Not img_id'})
        try:
            img = TopicImage.objects.get(id=img_id, user=user)
            img.delete()
        except Exception as e:
            return JsonResponse({'code': 10240, 'error': str(e)})
        return ({'code': 200})

