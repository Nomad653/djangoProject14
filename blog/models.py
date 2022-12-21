from django.db import models


from django.shortcuts import render
# Create your models here.
#
class Post(models.Model):
    title = models.CharField(max_length=255,null=False,blank=False)
    content = models.TextField(max_length=1400)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title