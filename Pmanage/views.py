from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login as lagin, logout as Lout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project, User, Tasks
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
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
    # print("percentage ",taskper)
    taskid=id
    print('int: ',taskid)
    taskperupdate=Tasks.objects.filter(id=id).update(taskpercentage=taskper)
    # get the project
    # test=sum(lst) / len(lst)
    # Average percentage update.
    updateperpro(taskid)
  
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
    

def track(request):
    proj=Project.objects.all()
    return render(request, "Pmanage/Track.html",{"proj": proj})
    
@csrf_exempt
def release(request):
    id=request.body
    project_id=json.loads(id)
    project=Project.objects.filter(id=project_id)
    for projects in project:
        print(f'{projects.id} is {projects.Project_name}')
        pro
    return  JsonResponse({"proj":"proj"})


def report(request):
    return render(request, "Pmanage/Report.html")
