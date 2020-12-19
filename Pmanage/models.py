from django.db import models

# Create your models here.
class Project(models.Model):
    Project_name=models.CharField(max_length=64)
    tasks=models.IntegerField()
    team=models.IntegerField()
    def __str__():
        return f'{Project_name}'
