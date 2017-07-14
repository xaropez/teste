from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime
# Create your views here.

def va_hora(request):
    now = datetime.datetime.now()
    message = "Hi, finally i got it"
    html = "<html><body> %s </body></html>" % message
    return HttpResponse(html)
    #return TemplateResponse(request, 'horas/index.html', {})