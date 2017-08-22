from django.http import HttpResponse


def index(index):
    return HttpResponse('这是选举应用的首页')

