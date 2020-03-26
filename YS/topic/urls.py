from django.conf.urls import url

from topic import views

urlpatterns = [
    # http://127.0.0.1:8000/api/v1/topics
    url(r'^$', views.handle_topics),
    # http://127.0.0.1:8000/api/v1/topics/t_id/<t_id>
    url(r'^/t_id/(?P<t_id>\w+)$', views.handle_topics),
    # http://127.0.0.1:8000/api/v1/topics/u_id/<u_id>
    url(r'^/u_id/(?P<u_id>\w+)$', views.handle_topics),
    # http://127.0.0.1:8000/api/v1/topics/collect/t_id
    url(r'^/collect(/u_id/(?P<u_id>\w+))?$', views.collect_topics),


]