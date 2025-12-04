from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from .models import Post

# posts=[
#         {'id':1,'title':'Object Oriented Programming','content':'OOP is one of the important concept..','tag':'#Programming'},
#         {'id':2,'title':'Version Control','content':'Git and GitHub is used in version control','tag':'#DevOps'},
#         {'id':3,'title':'Web Development','content':'HTML, CSS and Javascript is used in web development..','tag':'#Web-Dev'},
#         {'id':4,'title':'AI for Students','content':'AI is one of the evolving field in tech. It\'s important to learn it.','tag':'#AI'}
#     ]

def index(request):
    blog_title="Latest Posts"
    posts=Post.objects.all() # getting data from post model
    return render(request,'index.html',{'blog_title':blog_title,'posts':posts})

def detail(request,slug):
    # static list of posts
    # post=next((item for item in posts if item['id'] == int(post_id)),None)
    
    # getting data from post model
    try:
        post=Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("This Post does not Exist")
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post['title']}')
    return render(request,'details.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URl")

