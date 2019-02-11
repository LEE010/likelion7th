from django.shortcuts import render
from .models import Blog

def home(request):
    blogs_all = Blog.objects.all() # query set!
    blogs = Blog.objects
    return render(request, 'home.html',{'blogs':blogs,'blogs_all':blogs_all})
