from django.conf.urls import url

from ytoken import views


urlpatterns = [
    url(r'^$', views.ytoken)
]