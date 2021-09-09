from django.contrib import admin
from django.urls import path,include
from blog import views
urlpatterns = [
    path("",views.index,name="index"),
    path("create/",views.write,name="write"),
    path("detail/<blog_id>",views.detail,name="detail")
]