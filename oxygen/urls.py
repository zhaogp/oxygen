"""
URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.auth.views import login
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^maths/', include('maths.urls')),
    # url(r'^polls/', include('polls.urls')),
    # url(r'^weixin/', include('weixin.urls')),
]
