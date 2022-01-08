from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_up = models.DateTimeField(auto_now_add=True) 
    updated_up = models.DateTimeField(auto_now=True)
