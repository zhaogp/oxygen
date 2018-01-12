from django.shortcuts import render, redirect
import logging
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages


logger = logging.getLogger(__name__)

def index(request):
    logger.debug('Enter index view') 
    return render(request, 'oxygen/index.html')

def login(request):
    logger.debug('Enter login view')
    if request.method == 'POST':
        logger.debug('post request')
        form = LoginForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
            logger.info('form is valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                logger.info('%s login' % username)
                auth_login(request, user)
                return redirect('index')  # redirect to home page
            else:
                logger.error('Incorrect username or password.')
                messages.add_message(request, messages.ERROR, 'Incorrect username or password.')
                return render(
                    request, 
                    'oxygen/login.html', 
                    {
                        'form': form, 
                        'error_messages': messages.get_messages(request)
                    }
                )
                
    else:
        logger.info('return unbound form')
        return render(request,'oxygen/login.html', {'form': LoginForm()})

def register(request):
    logger.info('Enter register view')
    return render(request, 'oxygen/register.html')
