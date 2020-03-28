from django.conf.urls import url

from todo import views

urlpatterns = [
    # todos/test
    url(r'^test$', views.test),
    # todos/u_id/<u_id>
    # url(r'^$', views.get_index_todos),
    # todos/day/<day>
    url(r'^day(/(?P<day>\w+))?$', views.day_todos),
    # todos/week/<week>
    # url(r'^week/(?P<week>\w+)$', views.week_todos),
    # todos/month/<month>
    # url(r'^month/(?P<month>\w+)$', views.month_todos),
    # todos/day/<day>
    # url(r'^year/(?P<year>\w+)$', views.year_todos),


]