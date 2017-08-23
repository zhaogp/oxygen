from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def index(request):
    all_questions = Question.objects.all()
    context = {'all_questions': all_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    pass
