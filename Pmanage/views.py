from django.shortcuts import render, HttpResponse,HttpResponseRedirect,reverse
from django.contrib.auth import authenticate, login as lagin, logout as Lout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project,User


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "Pmanage/index.html")
    else:
        return render(request, "Pmanage/login.html")


def login(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        print(username, 'and', password)
        struser = str(username)
        strpass = str(password)
        user = authenticate(request,username=struser, password=strpass)
        if user is not None:
            lagin(request, user)
            return render(request, "Pmanage/index.html")
        else:
            return render(request, "Pmanage/login.html")
    return HttpResponse("wer")

@login_required()
def logout(request):
    Lout(request)
    return render(request, "Pmanage/logout.html")



@login_required
def createproject(request):
    return render(request, "Pmanage/Plan.html")

@login_required
def plan(request):
    project_title=request.POST["Pname"]
    team=request.POST["team"]
    maxday=request.POST["maxday"]
    print(project_title,"",team,"",maxday)
    projects=Project.objects.all()
    return render(request, "Pmanage/createplan.html",{
        "projects":projects
    })

@login_required
def create_plan(request,id):
    return render(request,"Pmanage/createplan.html")

def track(request):
    return render(request, "Pmanage/Track.html")


def release(request):
    return render(request, "Pmanage/Release.html")


def report(request):
    return render(request, "Pmanage/Report.html")
