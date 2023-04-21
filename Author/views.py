from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import News, Category
from .form import NewsForm,CategoryForm
from advertiser.models import Ads,Advertiser
from django.contrib.auth import logout as auth_logout, login as auth_login,authenticate
# Create your views here.

def login(request):
    context={}
    context["title"]="Login"
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if username and password:
            user=authenticate(request,username=username,password=password)
            if user:
                auth_login(request,user)
                return redirect("auth_home")
            else :
                context["message"]="invalid password"
                return render(request,"admin/login.html",context=context)
        else:
            context["message"]="Enter username and password"
            return render(request,"admin/login.html",context=context)
    return render(request,"admin/login.html",context=context)
 
def is_admin(request):
    if request.user.is_authenticated:
        return not (request.user.username[2:].isnumeric() and request.user.username[:2]=="ad")
    else :
        return False
    
def home(request):
    if not is_admin(request):
        return redirect("auth_login")
    return render(request,"admin/main.html")

def logout(request):
    auth_logout(request)
    return redirect("auth_login")
def viewnews(request):
    if not is_admin(request):
        return redirect("auth_login")
    context={"news":News.objects.all()}
    return render(request,"admin/news.html",context)

def addnews(request):
    context={}
    if not is_admin(request):
        return redirect("auth_login")
    if request.method=="POST":
        form=NewsForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            context["message"]="added"
            return render(request,"tmform.html",context)
        else:
            context["form"]=NewsForm(request.POST,request.FILES)
            return render(request,"tmform.html",context)
    else:
        context["form"]=NewsForm(request.POST,request.FILES)
        return render(request,"newpost.html",context)

def editnews(request,id):
    context={}
    if not is_admin(request):
        return redirect("auth_login")
    if request.method=="POST":
        form=NewsForm(request.POST,request.FILES)
        if form.is_valid() :
            data=form.save(commit=False)
            data.id=id
            data.save()
            context["message"]="added"
            return render(request,"tmform.html",context)
        else:
            context["form"]=NewsForm(request.POST,request.FILES)
            return render(request,"tmform.html",context)
    else:
        objectdata=News.objects.get(id=id)
        context["form"]=NewsForm(instance=objectdata)
        return render(request,"newpost.html",context)

def removenews(request,id):
    News.objects.get(id=id).delete()
    return redirect("viewnews")
def viewcategory(request):
    if not is_admin(request):
        return redirect("auth_login")
    context={"category":Category.objects.all()}
    return render(request,"admin/category.html",context)

def addcategory(request):
    if not is_admin(request):
        return redirect("auth_login")
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
        return redirect("auth_login")
    ads=Ads.objects.all()
    for i in ads:
        if i.status == 0:
            i.status = "pending"
        elif i.status == 1 :
            i.status = "accept"
        else :
            i.status = "removed"

    context={"post":ads}
    return render(request,"admin/post.html",context)

def advertiser(request):
    if not is_admin(request):
        return redirect("auth_login")
    context={"adv":Advertiser.objects.all()}
    return render(request,"admin/advertiser.html",context)
def rejectpost(request,id):
    if not is_admin(request):
        return redirect("auth_login")
    ob=Ads.objects.get(id=id)
    ob.status=2
    ob.save()
    return redirect("post")

def acceptpost(request,id):
    if not is_admin(request):
        return redirect("auth_login")
    ob=Ads.objects.get(id=id)
    ob.status=1
    ob.save()
    return redirect("post")

