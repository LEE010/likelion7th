from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs_all = Blog.objects.all() # query set!
    blogs = Blog.objects
    return render(request, 'home.html',{'blogs':blogs,'blogs_all':blogs_all})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)

    return render(request,'detail.html',{'blog':blog_detail})
