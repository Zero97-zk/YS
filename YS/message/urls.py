from django.conf.urls import url

from message import views

urlpatterns = [
    # messages/test
    # url(r'^test$', views.test)
    # http://127.0.0.1:8000/api/v1/messages
    # http://127.0.0.1:8000/api/v1/messages/t_id/<t_id>
    url(r'^(t_id/(?P<t_id>\d+))?$', views.handle_messages),
    # message/reply
    url(r'^reply$', views.handle_replys)
]