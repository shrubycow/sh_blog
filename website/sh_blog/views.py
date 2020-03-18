from django.shortcuts import render
from .models import Post, Rubric
from precise_bbcode.bbcode import get_parser
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

# Create your views here.

def bb_parse(elements):
    parser = get_parser()
    try:
        iter(elements)
        for element in elements:
            element.body = parser.render(str(element.body))
    except TypeError:
        elements.body = parser.render(str(elements.body))
    return elements

def index(request):
    posts = Post.objects.order_by('-created').filter(status='published')[:5]
    posts = bb_parse(posts)
    return render(request, 'sh_blog/index.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    post = bb_parse(post)
    return render(request, 'sh_blog/detail.html', {'post': post})

def not_about_work(request):
    rubrics = Rubric.objects.filter()
    return render(request, 'sh_blog/not_work.html', {'rubrics': rubrics})

def by_rubric(request, pk):
    posts = Post.objects.filter(rubric__id=pk).filter(status='published')
    posts = bb_parse(posts)
    rubric = Rubric.objects.get(id=pk)
    return render(request, 'sh_blog/by_rubric.html', {'posts': posts, 'rubric': rubric})