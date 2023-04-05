from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import News, Category
from .form import NewsForm,CategoryForm
from advertiser.models import Ads,Advertiser
# Create your views here.
def viewnews(request):
    context={"news":News.objects.all()}
    return render(request,"admin/news.html",context)

def addnews(request):
    context={}
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
        return render(request,"tmform.html",context)

def viewcategory(request):
    
    context={"category":Category.objects.all()}
    return render(request,"admin/category.html",context)

def addcategory(request):
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
    context={"post":Ads.objects.all()}
    return render(request,"admin/post.html",context)

def advertiser(request):
    context={"adv":Advertiser.objects.all()}
    return render(request,"admin/advertiser.html",context)
def rejectpost(request,id):
    ob=Ads.objects.get(id=id)
    ob.status=2
    ob.save()
    return redirect("post")

def acceptpost(request,id):
    ob=Ads.objects.get(id=id)
    ob.status=1
    ob.save()
    return redirect("post")



