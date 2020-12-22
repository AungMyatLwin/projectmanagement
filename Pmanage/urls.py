
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="Index"),
    path('login',views.login,name="Login"),
    path('logout',views.logout,name="Logout"),
    path("createproject",views.createproject,name="Create"),
    path("createplans",views.create_plan,name="Cplan"),
    path('plan',views.plan,name="Plan"),
    path('track',views.track,name="Track"),
    path('release',views.release,name="Release"),
    path('report',views.report,name="Report")
]