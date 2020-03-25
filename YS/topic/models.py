from django.db import models

from user.models import User
# Create your models here.

class Topics(models.Model):
    type = models.CharField('类型', max_length=20)
    title = models.CharField('标题', max_length=30)
    introduce = models.CharField('文章简述', max_length=50)
    content = models.TextField('文章内容')
    created_time  = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('修改时间', auto_now=True)
    like_count = models.IntegerField('点赞量', default=0)
    watch_count = models.IntegerField('观看量', default=0)
    collecton_count = models.IntegerField('收藏量', default=0)
    author = models.ForeignKey(User, related_name='author_id')
    like_user = models.ManyToManyField(User, related_name='like_user', through='TopicLikeUser', through_fields=('topic_id', 'user_id'))
    watch_user = models.ManyToManyField(User, related_name='watch_user', through='TopicWatchUser', through_fields=('topic_id', 'user_id'))

    class Meta:
        db_table = 'topic'

class TopicLikeUser(models.Model):
    user = models.ForeignKey(User, related_name='like_user_id')
    topic = models.ForeignKey(Topics, related_name='like_topic_id')

    class Meta:
        db_table = 'topiclikeuser'

class TopicWatchUser(models.Model):
    user = models.ForeignKey(User, related_name='watch_user_id')
    topic = models.ForeignKey(Topics, related_name='watch_topic_id')

    class Meta:
        db_table = 'topicwatchuser'



