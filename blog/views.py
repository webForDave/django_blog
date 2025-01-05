from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_blog.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    fields = ['title', 'body']
    model = Post
    template_name = 'edit_blog.html'