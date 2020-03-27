from django.db import models

# Create your models here.
from user.models import User
from topic.models import Topic


class Message(models.Model):
    content = models.CharField('内容', max_length=200)
    created_time = models.DateTimeField('评论时间', auto_now_add=True)
    user = models.ForeignKey(User, related_name='messages')
    topic = models.ForeignKey(Topic, related_name='messages')
    like_count = models.IntegerField('点赞数量', default=0)
    like_users = models.ManyToManyField(User, related_name='like_messages', through='MessageLike')
    reply_count = models.IntegerField('回复数量', default=0)

    class Meta:
        db_table = 'message'


class Reply(models.Model):
    content = models.CharField('内容', max_length=50)
    created_time = models.DateTimeField('回复时间', auto_now_add=True)
    user = models.ForeignKey(User, related_name='replys')
    message = models.ForeignKey(Message, related_name='replys')
    is_second_reply = models.BooleanField('是二级回复', default=False)
    parent_reply = models.ForeignKey('self', related_name='child_replys', null=True)
    like_users = models.ManyToManyField(User, related_name='like_replys', through='ReplyLike')
    like_count = models.IntegerField('点赞数量', default=0)
    reply_count = models.IntegerField('回复数量', default=0)

    class Meta:
        db_table = 'reply'

class MessageLike(models.Model):
    user = models.ForeignKey(User, related_name='message_likes')
    message = models.ForeignKey(Message, related_name='message_likes')

    class Meta:
        db_table = 'messagelike'


class ReplyLike(models.Model):
    user = models.ForeignKey(User, related_name='reply_likes')
    reply = models.ForeignKey(Reply, related_name='reply_likes')

    class Meta:
        db_table = 'replylike'


