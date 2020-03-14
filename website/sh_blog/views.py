from django.shortcuts import render
from .models import Post, Rubric
from precise_bbcode.bbcode import get_parser
# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created')[:5]
    return render(request, 'sh_blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'sh_blog/detail.html', {'post': post})

def not_about_work(request):
    rubrics = Rubric.objects.all()
    return render(request, 'sh_blog/not_work.html', {'rubrics': rubrics})