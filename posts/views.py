from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("wellcome to django")


def home(request):
    return HttpResponse('<h3>wellcome to my blog....</h3>')