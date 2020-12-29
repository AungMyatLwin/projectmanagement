from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login as lagin, logout as Lout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project, User, Tasks,Report
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
import json
import hashlib
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "Pmanage/index.html")
    else:
        return render(request, "Pmanage/login.html")

def register(request):
    f=UserForm()
    pf=f.as_p()
    return render(request, "Pmanage/register.html")
    
def reg_user(request):
    if request.method=="POST":
        usrn=request.POST["username"]
        email=request.POST["email"]
        pwd=request.POST["password"]
        print(f'{usrn} and {email} {pwd}')
        # django use pbdk2 algo with sha-256. 
        # make_password import from django.contrib.auth.hashers
        # will take care of it.
        password=make_password(pwd)
        print(password)
        Usr=User.objects.create(username=usrn,email=email,password=password)
        Usr.save()
        return HttpResponseRedirect(reverse(index))
    return HttpResponseRedirect(reverse(index))

def login(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        print(username, 'and', password)
        struser = str(username)
        strpass = str(password)
        user = authenticate(request, username=struser, password=strpass)
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
def projects(request):
    project = Project.objects.all()
    return render(request, "Pmanage/index.html", {
        "projects": project
    })


@login_required
# PID project ID
def intproject(request, id):
    showproject = Project.objects.filter(id=id)
    showtasks = Tasks.objects.filter(Pid=id)
    return render(request, "Pmanage/projectID.html", {
        "Project": showproject, "Tasks": showtasks
    })


# create project
@login_required
def createproject(request):
    return render(request, "Pmanage/Plan.html")


@login_required
# project create
def plan(request):
    project_title = request.POST["Pname"]
    team = request.POST["team"]
    maxday = request.POST["maxday"]
    p = Project.objects.create(Project_name=project_title, complete_percentage=1, team=team, max_day=maxday)
    p.save()
    # project created then redirect to
    print(project_title, "", team, "", maxday)
    projects = Project.objects.all()
    return render(request, "Pmanage/index.html", {
        "projects": projects
    })


@login_required
#Task create
def task(request,id):
    print(id)
    task_id=Tasks.objects.filter(id=id)
    print(task_id)
    return render(request, "Pmanage/task.html",{"projects":task_id})

# Task create
@login_required
def create_plan(request, id):
    addtask = request.POST["task1"]
    pid=int(id)
    tadd=Tasks.objects.create(taskname=addtask,Pid_id=pid)
    tadd.save()
    return HttpResponseRedirect(reverse(intproject, args=[id]))

# id is not id its percentage
def task_percentage(request,id):
    taskper=request.GET.get('percentage')
    print(type(id))
    taskperupdate=Tasks.objects.filter(id=id).update(taskpercentage=taskper)
    updateperpro(id)
    return HttpResponseRedirect(reverse(task,args=[id]))

# get average percentage of the each given project
def updateperpro(id):
    li=list()
    # print(id)
    tsk=Tasks.objects.filter(id=id)
    for task in tsk:
        task_id=task.Pid_id
        pro=Tasks.objects.filter(Pid_id=task_id)
        for pros in pro:
            li.append(pros.taskpercentage)
    sums=sum(li)
    lens=len(li)
    average_complete_percentage=sums/lens
    update(task_id,average_complete_percentage)
    print("updated") 



def update(pid,avg):
    Project.objects.filter(id=pid).update(complete_percentage=avg)
    print("updated") 
    
@login_required
def track(request):
    proj=Project.objects.all()
    return render(request, "Pmanage/Track.html",{"proj": proj})
    
@login_required
@csrf_exempt
def release(request):
    id=request.body
    project_id=json.loads(id)
    projec=Project.objects.filter(id=project_id).update(status="release")
    return  JsonResponse({"proj":projec})

@login_required
def released(request):
    proj = Project.objects.filter(status="release")
    return render(request, "Pmanage/Release.html",{"proj": proj})

@login_required
def report(request):
    projec=Project.objects.filter(status="release")
    return render(request, "Pmanage/Report.html",{"projs":projec})

@login_required
@csrf_exempt
def reported(request,id):
    if request.method == "POST":
        text=request.POST["Report"]
        reports=Report.objects.create(proid_id=id,Reports=text)
        reports.save()
        return HttpResponseRedirect(reverse(report))
    if request.method == "GET":
        rett=[]
        xx=Report.objects.filter(proid_id=id)
        for r in xx:
            rett.append(r.Reports)
    return JsonResponse(rett,safe=False)
    
