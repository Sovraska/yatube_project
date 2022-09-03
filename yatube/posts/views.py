from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):

    template = 'posts/index.html'

    title = 'Yatube'
    text = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }

    return render(request, template, context)

def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context) 
