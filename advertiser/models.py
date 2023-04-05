from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Advertiser(models.Model):
    Company_Name=models.CharField( max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin=models.IntegerField()
    building_name=models.CharField(max_length=50)
    def __str__(self):
        return self.Company_Name
    

class AdsType(models.Model):
    Type=models.CharField(max_length=50)
    price=models.IntegerField()
    def __str__(self):
        return self.Type
    

class Ads(models.Model):
    advertiser=models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="ads", height_field=None, width_field=None, max_length=None)
    link=models.CharField(max_length=50)
    Type=models.ForeignKey(AdsType, on_delete=models.CASCADE)
    date=models.DateField(auto_now=False, auto_now_add=False)
    months=models.IntegerField()  
    status=models.IntegerField(default=0)
    #status 0 when pending
    #status 1 when accept
    #status 2 when removes
    