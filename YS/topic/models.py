from django.db import models

from user.models import User
# Create your models here.

class Topic(models.Model):
    type = models.CharField('类型', max_length=20)
    title = models.CharField('标题', max_length=30)
    introduce = models.CharField('文章简述', max_length=50)
    content = models.TextField('文章内容')
    created_time  = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)
    like_count = models.IntegerField('点赞量', default=0)
    watch_count = models.IntegerField('观看量', default=0)
    collect_count = models.IntegerField('收藏量', default=0)
    author = models.ForeignKey(User, related_name='topics')
    like_users = models.ManyToManyField(User, related_name='like_topics', through='TopicLikeUser')
    collect_users = models.ManyToManyField(User, related_name='collect_topics', through='TopicCollectUser')
    limit = models.CharField('权限', max_length=20, choices=(('public', '公开'), ('private', '不公开')), default='public')

    class Meta:
        db_table = 'topic'

class TopicLikeUser(models.Model):
    user = models.ForeignKey(User, related_name='like_id')
    topic = models.ForeignKey(Topic, related_name='like_id')

    class Meta:
        db_table = 'topiclikeuser'

class TopicCollectUser(models.Model):
    user = models.ForeignKey(User, related_name='collect_id')
    topic = models.ForeignKey(Topic, related_name='collect_id')

    class Meta:
        db_table = 'topiccollectuser'



