from django.db import models

# Create your models here.
class Project(models.Model):
    Project_name=models.CharField(max_length=64)
    task=models.IntegerField()
    team=models.IntegerField()
    complete_percentage=models.IntegerField()
    def __str__():
        return f'{Project_name}'

class Tasks(models.Model):
    projectid=models.ForeignKey(Project,on_delete=models.CASCADE)
    taskname=models.CharField(max_length=64)
    percentage=models.IntegerField()


