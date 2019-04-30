from django.shortcuts import render, get_object_or_404
from blog.models import Blog


# Create your views here.
def all_blogs(request):
    blogs = Blog.objects
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


# single blog view
def single_blog(request, blog_id):
    single_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/single.html', {'blog': single_blog})
