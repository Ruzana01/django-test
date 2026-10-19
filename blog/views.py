from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    # Передаем ключ 'blog' для цикла {% for i in blog %}
    return render(request, 'blog_list.html', {'blog': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    

    blog.likes += 1
    blog.save()
    
    # Передаем ключ 'blog_id' под переменную {{ blog_id.title }}
    return render(request, 'blog_detail.html', {'blog_id': blog})