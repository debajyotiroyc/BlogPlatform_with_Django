from django.contrib import admin
from django.urls import path,include
from blog import views
urlpatterns = [
    path("",views.index,name="index"),
    path("create/",views.write,name="write"),
    path("sign-up/",views.register,name="signup"),
    path("login/",views.loginuser,name="login"),
    path("logout/",views.logoutuser,name="logout"),
    #path("detail/<blog_id>",views.detail,name="detail"),
    path("<slug:slug>/",views.detail,name="detail"),
    path("profile/",views.profile,name="profile")
]
