from django.shortcuts import render
from django.http import HttpResponse
from posts.models import *
# Create your views here.


def index(request):
    return HttpResponse("wellcome to django")


def home(request):
    return HttpResponse('<h3>wellcome to my blog....</h3>')

def post_list(request):
    posts = post.objects.all()
    context = {"posts":posts}
    return render(request,"posts/post_list.html",context=context)

def post_view(request, post_id):
    posts = post.objects.get(pk = post_id)
    comments = comment.objects.filter(post=posts)
    context = {"post":posts,"comment":comments}
    return render(request,"posts/post_view.html",context=context)