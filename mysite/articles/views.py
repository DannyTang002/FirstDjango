from django.http import HttpResponse
from django.shortcuts import render
from.models import Article 
from django.contrib.auth.decorators import login_required


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')#the database of articles ordered by date 
    return render(request, "articles/article_list.html",{'articles':articles})
    #sends the data as a dir with the database to the used template

def article_detail(request,slug):
   article  = Article.objects.get(slug=slug)
   return render(request,'articles/article_detail.html',{'article':article})


@login_required(login_url="/accounts/login")
def article_create(request):
    return render(request,"articles/article_create.html" )