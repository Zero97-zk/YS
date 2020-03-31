from django.conf.urls import url

from user import views

urlpatterns =[
    # http://127.0.0.1/api/v1/users/test
    # url(r'test', views.test),
    # http://127.0.0.1:8000/api/v1/users
    url(r'^$', views.users),
    # http://127.0.0.1:8000/api/v1/users/<id>?nickname=1
    url(r'^(?P<id>\d+)$', views.users),
    # http://127.0.0.1:8000/api/v1/users/<id>/avatar
    url(r'^(?P<id>\d+)/avatar$', views.avatar),
    # http://127.0.0.1:8000/api/v1/users/login/<u_id>
    url(r'^avoid_login$', views.avoid_login)
    # http://127.0.0.1:8000/api/v1/users/<id>/change_password
    # url(r'^/(?P<id>\w+)/change_password$', views.change_password)
]