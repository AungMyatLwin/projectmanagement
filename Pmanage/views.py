from django.shortcuts import render,HttpResponse
from .models import Project
# Create your views here.
def index(request):
    print("gay")
    return render(request,"Pmanage/Plan.html")
    
def plan(request):
    return render(request,"Pmanage/Plan.html")

def track(request):
    return render(request,"Pmanage/Track.html")


def release(request):
    return render(request,"Pmanage/Release.html")

def report(request):
    return render(request,"Pmanage/Report.html")
