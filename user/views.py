from django.shortcuts import render
from Author.models import News,Category
from advertiser.models import Ads
# Create your views here.
def home(request):
    context={"news":News.objects.all(),"Category":Category.objects.all()}
    return render(request,"user/content.html",context)


def category(request,id):
    context={"news":News.objects.all().filter(Category_id=id),"Category":Category.objects.all(),"catsingle":Category.objects.get(id=id)}
    return render(request,"user/content.html",context)

def single(request,id):
    a=News.objects.get(id=id);
    a.views=a.views+1
    a.save()
    context={"news":a,"Category":Category.objects.all(),"ads":getads()}
    return render(request,"user/single.html",context)
import random
def getads():
    a=Ads.objects.all().filter(status=1)
    index=random.randint(0,Ads.objects.all().filter(status=1).count()-1)
    return a[index]