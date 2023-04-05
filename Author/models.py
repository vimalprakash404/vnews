from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class News(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100000)
    views=models.IntegerField()
    image=models.ImageField(upload_to="news", height_field=None, width_field=None, max_length=None)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    place=models.CharField(null=True, max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False,null=True)