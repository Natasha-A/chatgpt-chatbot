from django.shortcuts import render
from django.http import HttpResponse


# Home View
def home(request):
    return HttpResponse('The Home Page')
  
  
def new_chat(request):
  return HttpResponse('New Chat Page')


# Error View
def error_handler(request):
    return HttpResponse('404 Page')
