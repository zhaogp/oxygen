from django.conf.urls import url

from . import views


app_name = 'maths'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^algo/yue/$', views.yue, name='yue'),
    url(r'^algo/stack/$', views.stack, name='stack'),
]
