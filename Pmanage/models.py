from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Team_Member(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE,name="userid")
    team_members_firstname=models.CharField(max_length=64)
    team_members_lastname=models.CharField(max_length=64)
    team_leader=models.IntegerField()


class Team(models.Model):
    team=models.IntegerField()
    tem_member=models.ForeignKey(Team_Member,on_delete=models.CASCADE,name="Temid")

# Create your models here.
class Project(models.Model):
    Project_name=models.CharField(max_length=64)
    team=models.IntegerField()
    complete_percentage=models.IntegerField()
    createdate=datetime.datetime.now()
    max_day=models.IntegerField()

# Tasks with project id
class Tasks(models.Model):
    projectid=models.ForeignKey(Project,on_delete=models.CASCADE,name="Pid")
    taskname=models.CharField(max_length=64)

# Tracking status of each task
class Tracking(models.Model):
    taskid=models.ForeignKey(Tasks,on_delete=models.CASCADE,name="Tid")
    bugs=models.TextField()
    percentage=models.IntegerField()

# if Project.complete_percentage is 100 then release status will be update to "Released"
class Release(models.Model):
    projId=models.ForeignKey(Project,on_delete=models.CASCADE,name="proid")
    release_status=models.CharField(max_length=64)

class Report(models.Model):
    projectId=models.ForeignKey(Project,on_delete=models.CASCADE,name="proid")
    report=models.CharField(max_length=65,name="Error Description")
