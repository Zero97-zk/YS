from django.conf.urls import url

from topic import views

urlpatterns = [
    # http://127.0.0.1:8000/api/v1/topics
    url(r'^$', views.topics),
    # http://127.0.0.1:8000/api/v1/topics/t_id
    # url(r'^/(?P<t_id>\w+)$', views.topics)
]