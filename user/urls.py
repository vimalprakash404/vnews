from django.urls import path
from .views import *
urlpatterns = [
    path("",home),
    path("category/<int:id>",category),
    path("news/<int:id>",single)
]
