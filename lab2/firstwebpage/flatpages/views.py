from django.shortcuts import render
from django.http import HttpResponse
from django import template

def home(request):
    return HttpResponse(u'Hello World!', content_type="text/plain")
def home1(request):
    return HttpResponse(u'Hello World!123')    
def home2(request):
    return render(request, 'templates/static_handler.html')           

