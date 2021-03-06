"""YS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path, include
from django.conf.urls import url, include

from YS import settings

urlpatterns = [
    url(r'admin/', admin.site.urls),
    # http://127.0.0.1:8000/api/v1/users
    url(r'^api/v1/users/?', include('user.urls')),
    # http://127.0.0.1:8000/api/v1/ytoken
    url(r'^api/v1/ytoken/?', include('ytoken.urls')),
    # http://127.0.0.1:8000/api/v1/tipics
    url(r'^api/v1/topics/?', include('topic.urls')),
    # http://127.0.0.1:8000/api/v1/messages
    url(r'^api/v1/messages/?', include('message.urls')),
    # http://127.0.0.1:8000/api/v1/todos
    url(r'^api/v1/todos/?', include('todo.urls')),

]
