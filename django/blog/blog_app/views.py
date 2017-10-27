from django.shortcuts import render, get_object_or_404
from blog_app.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/home.html', {"posts": posts})

def single_post(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_app/single_post.html', {"posts": posts})
