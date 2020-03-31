from django.conf.urls import url

from todo import views

urlpatterns = [
    # todos/test
    # url(r'^test$', views.test),
    # todos
    url(r'^$', views.get_index_todos),
    # todos/day
    url(r'^day(/(?P<year>\d+)/(?P<day>\d+))?$', views.day_todos),
    # todos/week
    url(r'^week(/(?P<year>\d+)/(?P<week>\d+))?$', views.week_todos),
    # todos/month
    url(r'^month(/(?P<year>\d+)/(?P<month>\d+))?$', views.month_todos),
    # todos/year
    url(r'^year(/(?P<year>\d+))?$', views.year_todos),


]