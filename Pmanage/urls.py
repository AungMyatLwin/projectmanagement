
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="Index"),
    path('<int:id>/ProjectId',views.intproject,name="PID"),
    path('login',views.login,name="Login"),
    path('logout',views.logout,name="Logout"),
    path('Register',views.register,name="Register"),
    path("createproject",views.createproject,name="Create"),
    path("<int:id>/createplans",views.create_plan,name="Cplan"),
    path('projects',views.projects,name='All_Project'),
    path('<int:id>/Project',views.intproject,name="PID"),
    path('<int:id>/task',views.task,name="inditask"),
    path('<int:id>/TaskPercentage',views.task_percentage,name="Ptask"),
    path('plan',views.plan,name="Plan"),
    path('track',views.track,name="Track"),
    path('release',views.release,name="Release"),
    path("Released",views.released,name="Released"),
    path('<int:id>/reports',views.reported,name='reported')
    ,path('report',views.report,name="Report"),
    path('Create_User',views.reg_user,name="CreateUser")
]