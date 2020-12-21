from django.contrib import admin
from .models import Team,Team_Member,Tracking,Tasks,Project,Release,Report
# Register your models here.
admin.site.register(Team)
admin.site.register(Team_Member)
admin.site.register(Tracking)
admin.site.register(Tasks)
admin.site.register(Project)
admin.site.register(Release)
admin.site.register(Report)