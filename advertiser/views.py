from django.shortcuts import render,redirect
from .form import AdvertiserForm,AdsForm,AdsTypeForm,AddAdvertiserLoginTable
from .models import Ads,AdsType
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    context={}
    if request.method=="POST":
        form=AdvertiserForm(request.POST)
        form1=AddAdvertiserLoginTable(request.POST)
        if form.is_valid() and form1.is_valid():
            data=form.save()
            userob=form1.save(commit=False)
            userob.username="ad"+str(data.id)
            userob.save()
            context["message"]="added"
            return render(request,"tmform.html",context)
        else:
            context["form"]=AdvertiserForm(request.POST)
            context["form1"]=AddAdvertiserLoginTable(request.POST)
            context["message"]="invalid data please enter details"
            return render(request,"tmform.html",context)
    context["form"]=AdvertiserForm()
    context["form1"]=AddAdvertiserLoginTable()
    return render(request,"tmform.html",context)

def home(request):
    return render(request,"advertiser/home.html")

def is_advertiser(request):
    if request.user.is_authenticated:
        return (request.user.username[2:].isnumeric() and request.user.username[:2]=="ad")
    else :
        return (False)
    
    

def addposttype(request):
    if not is_advertiser(request):
        return redirect("login")
    context={}
    if request.method=="POST":
        form=AdsTypeForm(request.POST)
        if form.is_valid() :
            form.save()
            context["message"]="added"
            context["form"]=AdsTypeForm(request.POST)
            return render(request,"tmform.html",context)
        else:
            context["form"]=AdsTypeForm(request.POST)
            context["message"]="added"
            return render(request,"tmform.html",context)
    else:
        context["form"]=AdsTypeForm(request.POST)
        return render(request,"tmform.html",context)

def postads(request):
    if not is_advertiser(request):
        return redirect("login")
    context={}
    if request.method=="POST":
        form=AdsForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            context["message"]="added"
            context["form"]=AdsForm(request.POST,request.FILES)
            return render(request,"advertiser/tmform.html",context)
        else:
            context["form"]=AdsForm(request.POST)
            context["message"]="added"
            return render(request,"advertiser/tmform.html",context)
    else:
        context["form"]=AdsForm(request.POST,request.FILES)
        return render(request,"advertiser/tmform.html",context)

def viewads(request):
    if not is_advertiser(request):
        return redirect("login")
    ads=Ads.objects.all().filter(advertiser_id=int(request.user.username[2:]))
    for i in ads:
        if i.status == 0:
            i.status = "pending"
        elif i.status == 1 :
            i.status = "accept"
        else :
            i.status = "removed"
    context={"ads":ads}
    return render(request,"advertiser/post.html",context)


def viewtype(request):
    if not is_advertiser(request):
        return redirect("login")
    types=AdsType.objects.all()
    return HttpResponse(types)

def login(request):
    context={}
    context["title"]="Login"
    if request.method=="POST":
        email=request.POST["username"]
        password=request.POST["password"]
        username=User.objects.get(email=email).username
        if username and password:
            user=authenticate(request,username=username,password=password)
            if user:
                auth_login(request,user)
                return redirect("viewads")
            else :
                context["message"]="invalid password"
                return render(request,"admin/login.html",context=context)
        else:
            context["message"]="Enter username and password"
            return render(request,"admin/login.html",context=context)
    return render(request,"admin/login.html",context=context)