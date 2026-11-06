from django.shortcuts import render

from .models import Post


def home_view(request):
    latest_posts = Post.objects.all()[:3]
    return render(request, 'home.html', context={'latest_posts': latest_posts})


def post_list_view(request):
    post_list = Post.objects.all()
    return render(request, 'posts.html', context={'posts':post_list})
