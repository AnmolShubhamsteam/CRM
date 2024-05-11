from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from core.models import *
from core.form import sign_up_form
# Create your views here.
def home(request):
    return render(request,"home.html")

def log_in(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
    return render(request,"login.html",{})
def log_out(request):
    logout(request)
    return redirect("login")

def Register_user(request):
    form=sign_up_form(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect("home")
    context={"form":form}
    return render(request,"register.html",context)
