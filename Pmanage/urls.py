
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="Index"),
    path('<int:id>/ProjectId',views.intproject,name="PID"),
    path('login',views.login,name="Login"),
    path('logout',views.logout,name="Logout"),
    path("createproject",views.createproject,name="Create"),
    path("<int:id>/createplans",views.create_plan,name="Cplan"),
    path('projects',views.projects,name='All_Project'),
    path('<int:id>/Project',views.intproject,name="PID"),
    path("Tasks",views.tasks,name="Task"),
    path('plan',views.plan,name="Plan"),
    path('track',views.track,name="Track"),
    path('release',views.release,name="Release"),
    path('report',views.report,name="Report")
]