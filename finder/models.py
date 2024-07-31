from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Keyword(models.Model):
    
    keyword = models.CharField(max_length=50)
    
    def __str__(self):
        return self.keyword
    
    
    
class SearchResult(models.Model):
    
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    publisher = models.TextField()
    content = models.TextField()
    publication_date = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)
    newCounter = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.publisher

class Agenda(models.Model):
    
    title = models.CharField(max_length=100)
    share = models.CharField(max_length=100)
    checkedDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
