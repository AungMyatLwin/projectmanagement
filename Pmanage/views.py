from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login as lagin,logout as Lout
from django.contrib.auth.models import User
from .models import Project
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST["Username"]
        password=request.POST["Password"]
        print(username,'and', password)
        struser=str(username)
        strpass=str(password)
        user = authenticate(username=struser, password=strpass)
        lagin(request,user)
        return render(request,"Pmanage/index.html")
    return HttpResponse("wer")

def logout(request):
    Lout(request)
    return render(request,"Pmanage/logout.html")

def index(request):
    return render(request,"Pmanage/login.html")
    
def plan(request):
    return render(request,"Pmanage/Plan.html")

def track(request):
    return render(request,"Pmanage/Track.html")


def release(request):
    return render(request,"Pmanage/Release.html")

def report(request):
    return render(request,"Pmanage/Report.html")
