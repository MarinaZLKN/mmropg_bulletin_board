from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-datecreation'
    template_name = 'posts.html'
    context_object_name = 'posts'