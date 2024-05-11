from django.contrib import admin
from django.urls import path
from core.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("login/",log_in,name="login"),
    path("logout/",log_out,name="logout"),
    path("register/",Register_user,name="register"),
    path("addinfo/",Addinfo,name="addinfo"),
    path("singledetail/<int:pk>/",singledetail,name="singledetail"),
    path("delete/<str:pk>/",delete_user,name="delete"),
    path("edit/<str:pk>/",edit,name="edit")
]
