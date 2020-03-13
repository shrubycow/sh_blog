from django.shortcuts import render
from .models import Post
from precise_bbcode.bbcode import get_parser
# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created')[:5]
    return render(request, 'sh_blog/index.html', {'posts': posts})