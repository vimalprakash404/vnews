from django.urls import path
from .views import *
urlpatterns = [
    path("reg", register, name="ad_register"),
    path("add/post", postads, name="postads"),
    path("add/type/", addposttype),
    path("view/type/", viewtype),
    path("view/post", viewads, name="viewads"),
    path("login/", login, name="login"),
    path("payment/<int:id>", payment_view, name="payment_view"),
    path("payment_fail/<int:id>", payment_failed, name="payment_failed"),
    path("payment_success/<int:id>", payment_success, name="payment_success"),
    path("logout", logout),
    path("", home, name="ad_home")
]
