import random
from django.shortcuts import render,redirect
from Author.models import News, Category
from advertiser.models import Ads
from django.contrib.auth import logout as auth_logout
# Create your views here.


def home(request):
    context = {"news": News.objects.all(
    ), "Category": Category.objects.all(), "ads": getads(type=2)}
    return render(request, "user/content.html", context)


def category(request, id):
    context = {"news": News.objects.all().filter(Category_id=id),
               "Category": Category.objects.all(), "catsingle": Category.objects.get(id=id),"ads": getads(type=2)}
    return render(request, "user/content.html", context)


def single(request, id):
    a = News.objects.get(id=id)
    a.views = a.views+1
    a.save()
    context = {"news": a, "Category": Category.objects.all(),
               "ads": getads(type=1)}
    return render(request, "user/single.html", context)


def getads(type):
    a = Ads.objects.all().filter(status=1, Type_id=int(type))
    index = random.randint(0, Ads.objects.all().filter(status=1, Type_id=int(type)).count()-1)
    return a[index]

def logout(request):
    auth_logout(request)
    return redirect("/ad/login/")