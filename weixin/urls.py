from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'verify', views.verify, name='verify')
]