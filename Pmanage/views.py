from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login,logout as Lout
from .models import Project
# Create your views here.
def login(request):
    return render(request,"Pmanage/login.html")

def logout(request):
    Lout(request)
    return render(request,"Pmanage/logout.html")

def index(request):
    return render(request,"Pmanage/index.html")
    
def plan(request):
    return render(request,"Pmanage/Plan.html")

def track(request):
    return render(request,"Pmanage/Track.html")


def release(request):
    return render(request,"Pmanage/Release.html")

def report(request):
    return render(request,"Pmanage/Report.html")
