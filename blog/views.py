from django.shortcuts import render,redirect
from .models import Blog,Comment
from .forms import BlogForm,CommentForm
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request,"index.html",context)

def write(request):
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

def detail(request,blog_id):
    post=Blog.objects.get(pk=blog_id)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            print("ok")
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("detail",blog_id=blog_id)
    else:
        form=CommentForm()
    context={'post':post,'form':form}
    return render(request,"post_detail.html",context)
