from django.shortcuts import render,redirect
from .models import Blog,Comment
from .forms import BlogForm,CommentForm,UserForm,User
from django.contrib.auth import authenticate, logout,login


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request,"index.html",context)

def write(request):
    if request.user.is_anonymous:
        return redirect("signup")
    blogs=Blog.objects.all()
    if request.method=="POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            print("ok")
            form.save()
            return redirect("index")
    else:
        form = BlogForm()
    context={'blogs':blogs,'form':form}
    return render(request,"create.html",context)

def detail(request,slug):
    if request.user.is_anonymous:
        return redirect("signup")
    post=Blog.objects.get(slug=slug)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            print("ok")
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("detail",slug=slug)
    else:
        form=CommentForm()
    context={'post':post,'form':form}
    return render(request,"post_detail.html",context)


def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            print("ok")
            form.save()
            return redirect("index")
    else:
        form=UserForm()
    context={'form':form}
    return render(request,"register.html",context)

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            print("ok")
            login(request,user)
            return redirect("index")
        else:
            return render(request, 'log_in.html')

    return render(request, 'log_in.html')

def logoutuser(request):
    logout(request)
    return redirect("login")

def profile(request):
    if request.user.is_anonymous:
        return redirect("signup")
    account = request.user
    context = {'account': account}
    return render(request,"profile.html",context)


