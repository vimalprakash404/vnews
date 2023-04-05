from django.urls import path
from .views import *
urlpatterns = [
    path("view/news",viewnews,name="viewnews"),
    path("view/category",viewcategory,name="viewcategory"),
    path("view/post",post,name="post"),
    path("view/adv",advertiser,name="advertiser"),
    path("add/news",addnews,name="addnews"),
    path("add/category",addcategory,name="addcategory"),
    path("test",test),
    path("post/accept/<int:id>",acceptpost,name="acceptpost"),
    path("post/remove/<int:id>",rejectpost,name="rejectpost"),
]
