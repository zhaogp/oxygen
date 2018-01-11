from django.shortcuts import render
import logging
from .forms import LoginForm


logger = logging.getLogger(__name__)

def index(request):
    logger.info('Enter project index view') 
    return render(request, 'oxygen/index.html')

def login(request):
    logger.info('Enter login view')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            logger.info('username: %s, password: %s' % (username, password)) 
    else:
        form = LoginForm()
    
    return render(request,'oxygen/login.html', {'form': form})

def register(request):
    logger.info('Enter register view')
    return render(request, 'oxygen/register.html')
