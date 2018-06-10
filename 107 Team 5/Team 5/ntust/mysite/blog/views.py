from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from . import models
import datetime


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html')

# def category(request):
#     pid=request.GET["id"]
#     posts = Post.objects.filter(category=pid)
#     categories = Category.objects.all()
#     return render(request, 'blog/category.html', {'posts': posts,'categories':categories})

def view(request):

    pid = request.POST.get('id', False);
    posts = Post.objects.filter(p_id = pid)
    latest_cards_list = Comment.objects.filter(post = pid)

    return render(request, 'blog/shop1.html', {'posts': posts,'latest_cards_list':latest_cards_list,'pid':pid})

def post_comment(request,p_id):
    pid=p_id
    c_title =request.POST['c_title']
    c_user_name = request.POST['c_user_name']
    c_content = request.POST['c_content']
    c_pub_date = datetime.datetime.now()
    cards = models.Comment(title=c_title,user_name=c_user_name,content=c_content,pub_date=c_pub_date,post=pid)
    cards.save()
    return HttpResponseRedirect('/blog/view/?id=%s'%pid)

def shop1(request):
    posts = Post.objects.get(p_id=1)
    return render(request,'blog/shop1.html',{'posts':posts})

def shop2(request):

    posts = Post.objects.get(p_id=3)
    return render(request,'blog/shop1.html',{'posts':posts})

def shop3(request):

    posts = Post.objects.get(p_id=4)
    return render(request,'blog/shop3.html',{'posts':posts})