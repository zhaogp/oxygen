import logging

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages

from .forms import LoginForm, SignupForm

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Enter index view') 
    return render(request, 'oxygen/index.html')
