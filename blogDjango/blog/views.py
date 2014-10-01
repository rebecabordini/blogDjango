from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
import datetime


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': posts_publicados_no_passado()
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def posts_publicados_no_passado():
    posts = []
    for post in Blog.objects.all():
        if (post.get_data_publicacao() <= datetime.datetime.now().date()):
            posts.append(post)
    return posts
