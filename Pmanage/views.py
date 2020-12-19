from django.shortcuts import render,HttpResponse
from .models import Project
# Create your views here.
def index(request):
    b=Project.objects.all()
    for na in b:
        name=na.Project_name
    return HttpResponse(f'<h1>Hello{name}</h1>')
    
def plan(request):
    return HttpResponse("<h1>Hello</h1>")

def tract(request):
    return HttpResponse("<h1>Hello</h1>")

def release(request):
    return HttpResponse("<h1>Hello</h1>")

def report(request):
    return HttpResponse("<h1>Hello</h1>")
