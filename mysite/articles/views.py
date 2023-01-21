from django.shortcuts import render
from.models import Article 

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')#the database of articles ordered by date 
    return render(request, "articles/article_list.html",{'articles':articles})
    #sends the data as a dir with the database to the used template