from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question

def index(request):
    all_questions = Question.objects.all()
    context = {'all_questions': all_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('不存在该问题')
    return render(request, 'polls/detail.html', {'question': question})
    
