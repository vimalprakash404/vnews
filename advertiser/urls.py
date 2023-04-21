from django.urls import path
from .views import *
urlpatterns = [
    path("reg",register,name="ad_register"),
    path("add/post",postads,name="postads"),
    path("add/type/",addposttype),
    path("view/type/",viewtype),
    path("view/post",viewads,name="viewads"),
    path("login/",login,name="login"),
    path("logout",logout),
    path("",home,name="ad_home")
]
