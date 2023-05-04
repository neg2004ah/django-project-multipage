from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Post(models.Model):
    image = models.ImageField(upload_to='blog',default='default.jpg')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tags)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    counted_views = models.IntegerField(default=0)
    counted_comments = models.IntegerField(default=0)
    status = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    
    class Meta:
        ordering = ('-created_date',)
        
    def __str__(self):
        return self.title
    