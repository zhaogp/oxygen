from django.shortcuts import render


def index(request):
    return render(request, 'maths/index.html')

def detail(request):
    pass
