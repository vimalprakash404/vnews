from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import News, Category
from .form import NewsForm,CategoryForm
from advertiser.models import Ads,Advertiser
from django.contrib.auth import logout as auth_logout
# Create your views here.

def is_admin(request):
    if request.user.is_authenticated:
        return not (request.user.username[2:].isnumeric() and request.user.username[:2]=="ad")
    else :
        return False
    
def home(request):
    if not is_admin(request):
        return redirect("login")
    return render(request,"admin/main.html")

def logout(request):
    auth_logout(request)
    return redirect("login")
def viewnews(request):
    if not is_admin(request):
        return redirect("login")
    context={"news":News.objects.all()}
    return render(request,"admin/news.html",context)

def addnews(request):
    context={}
    if not is_admin(request):
        return redirect("login")
    if request.method=="POST":
        form=NewsForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            context["message"]="added"
            return render(request,"tmform.html",context)
        else:
            context["message"]="not added"
            return render(request,"tmform.html",context)
    else:
        context["form"]=NewsForm(request.POST,request.FILES)
        return render(request,"newpost.html",context)

def viewcategory(request):
    if not is_admin(request):
        return redirect("login")
    context={"category":Category.objects.all()}
    return render(request,"admin/category.html",context)

def addcategory(request):
    if not is_admin(request):
        return redirect("login")
    context={}
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid() :
            form.save()
            context["message"]="added"
            return render(request,"tmform.html",context)
        else:
            context["message"]="added"
            return render(request,"tmform.html",context)
    else:
        context["form"]=CategoryForm()
        return render(request,"tmform.html",context)
    
def test(request):
    return render(request,"admin/main.html")

def post(request):
    if not is_admin(request):
        return redirect("login")
    context={"post":Ads.objects.all()}
    return render(request,"admin/post.html",context)

def advertiser(request):
    if not is_admin(request):
        return redirect("login")
    context={"adv":Advertiser.objects.all()}
    return render(request,"admin/advertiser.html",context)
def rejectpost(request,id):
    if not is_admin(request):
        return redirect("login")
    ob=Ads.objects.get(id=id)
    ob.status=2
    ob.save()
    return redirect("post")

def acceptpost(request,id):
    if not is_admin(request):
        return redirect("login")
    ob=Ads.objects.get(id=id)
    ob.status=1
    ob.save()
    return redirect("post")



