from django.shortcuts import render,HttpResponse
from .models import Project
# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello</h1>')
    
def plan(request):
    return HttpResponse('<h1>Hello</h1>')

def track(request):
    return HttpResponse("<h1>Hello</h1>")

def release(request):
    return HttpResponse("<h1>Hello</h1>")

def report(request):
    return HttpResponse("<h1>Hello</h1>")
