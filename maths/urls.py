from django.conf.urls import url

from . import views


app_name = 'maths'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^[0-9]{4}/$', views.detail, name='detail'),
]
