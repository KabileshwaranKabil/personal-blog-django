from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    blog_title="Latest Posts"
    posts=[
        {'id':1,'title':'Object Oriented Programming','content':'OOP is one of the important concept..','tag':'#Programming'},
        {'id':2,'title':'Version Control','content':'Git and GitHub is used in version control','tag':'#DevOps'},
        {'id':3,'title':'Web Development','content':'HTML, CSS and Javascript is used in web development..','tag':'#Web-Dev'},
        {'id':4,'title':'AI for Students','content':'AI is one of the evolving field in tech. It\'s important to learn it.','tag':'#AI'}
    ]
    return render(request,'index.html',{'blog_title':blog_title,'posts':posts})

def detail(request,post_id):
    return render(request,'details.html')

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URl")

