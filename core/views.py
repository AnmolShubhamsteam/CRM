from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from core.models import *
from core.form import sign_up_form
from core.models import Record
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from core.form import Edit_Record
# Create your views here.
def home(request):
    records=Record.objects.all()
    context={"records":records}
    return render(request,"home.html",context)

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

@login_required
def Addinfo(request):
    if request.method=='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        address=request.POST.get("address")
        email=request.POST.get("floating_email")
        phone=request.POST.get("floating_phone")
        city=request.POST.get("city")
        state=request.POST.get("state")
        zipcode=request.POST.get("zipcode")
        if Record.objects.filter(first_name=first_name,last_name=last_name,email=email).exists():
            messages.info("class and name already exist")
        else:
            Record.objects.create(first_name=first_name,last_name=last_name,address=address,email=email,phone=phone,city=city,state=state,zipcode=zipcode)
        return redirect("home")
    return render(request,"Details.html",{})

@login_required
def singledetail(request,pk):
    detail = get_object_or_404(Record, pk=pk)
    context={"detail":detail}
    return render(request,"Singledetail.html",context)

@login_required
def delete_user(request,pk):
    rec=Record.objects.get(pk=pk)
    rec.delete()
    return redirect("home")
@login_required
def edit(request, pk):
    current_record = Record.objects.get(pk=pk)
    if request.method == "POST":
        form = Edit_Record(request.POST, instance=current_record)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = Edit_Record(instance=current_record)
    context = {"form": form}
    return render(request, "edit.html", context)



