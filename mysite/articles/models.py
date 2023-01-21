from django.db import models

# Create your models here.
class Article(models.Model):
    title =  models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add thumbnail and auhtor

    def __str__(self):#så att databasen visar att varje article riktar mot sin titel
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'#only want to show a certain amout of text