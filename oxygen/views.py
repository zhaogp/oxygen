from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)

def index(request):
    logger.info('Enter project index view') 
    return render(request, 'oxygen/index.html')
