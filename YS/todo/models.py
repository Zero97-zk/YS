import datetime

from django.db import models

# Create your models here.
from user.models import User


def get_default_time(option):
    today = datetime.datetime.now()
    if option == 'year':
        return today.year
    elif option == 'day':
        return today.timetuple()[7]
    elif option == 'month':
        return today.month
    elif option == 'week':
        return today.isocalendar()[1]

class DayTodo(models.Model):
    user = models.ForeignKey(User, related_name='daytodos')
    content = models.CharField('内容', max_length=50)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    year = models.IntegerField('年', default=get_default_time('year'))
    day = models.IntegerField('日', default=get_default_time('day'))
    level = models.CharField('代办等级', max_length=5, choices=(('a', '一级'), ('b', '二级'), ('c', '三级'), ('d', '四级')))
    state = models.CharField('状态', max_length=20, choices=(('todo', '代办'), ('completed', '完成')), default='todo')

    def get_default_year( option):
        today = datetime.datetime.now()
        if option == 'year':
            return today.year
        elif option == 'day':
            return today.day
    class Meta:
        db_table = 'daytodo'


class WeekTodo(models.Model):
    user = models.ForeignKey(User, related_name='weektodos')
    content = models.CharField('内容', max_length=50)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    year = models.IntegerField('年', default=get_default_time('year'))
    week = models.IntegerField('周', default=get_default_time('week'))
    level = models.CharField('代办等级', max_length=5, choices=(('a', '一级'), ('b', '二级'), ('c', '三级'), ('d', '四级')))
    state = models.CharField('状态', max_length=20, choices=(('todo', '代办'), ('completed', '完成')), default='todo')

    class Meta:
        db_table = 'weektodo'


class MonthTodo(models.Model):
    user = models.ForeignKey(User, related_name='monthtodos')
    content = models.CharField('内容', max_length=50)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    year = models.IntegerField('年', default=get_default_time('year'))
    month = models.IntegerField('月', default=get_default_time('month'))
    level = models.CharField('代办等级', max_length=5, choices=(('a', '一级'), ('b', '二级'), ('c', '三级'), ('d', '四级')))
    state = models.CharField('状态', max_length=20, choices=(('todo', '代办'), ('completed', '完成')), default='todo')

    class Meta:
        db_table = 'monthtodo'


class YearTodo(models.Model):
    user = models.ForeignKey(User, related_name='yeartodos')
    content = models.CharField('内容', max_length=50)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    year = models.IntegerField('年', default=get_default_time('year'))
    level = models.CharField('代办等级', max_length=5, choices=(('a', '一级'), ('b', '二级'), ('c', '三级'), ('d', '四级')))
    state = models.CharField('状态', max_length=20, choices=(('todo', '代办'), ('completed', '完成')), default='todo')

    class Meta:
        db_table = 'yeartodo'






