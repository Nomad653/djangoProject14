from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Post
# Create your views here.


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = "home.html"

class ShowPost(DetailView):
    model = Post
    template_name = "detail.html"