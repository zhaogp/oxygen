from django.shortcuts import render
from django.core.cache import cache
import logging

from .forms import YueForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'maths/index.html')

def detail(request):
    pass

def yue(request):
    if request.method == 'POST':
        form = YueForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            logger.info('%d mod %d' % (x, y))

            m = x % y
            while m:
                x = y
                y = m
                m = x % y
            
            logger.info('result: %d' % y) 
    else:
        form = YueForm()
        y = None
    
    return render(request,'maths/yue.html', {'form': form, 'y': y})
