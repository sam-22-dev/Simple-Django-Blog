from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




class PostList(ListView):
    model = Post



class PostDetails(DetailView):
    model = Post



class CreatPost(CreateView):
    model = Post
    fields = ['title','content','create_date','draft','tags','author','image']
    success_url = ('/blog')



class UpdatePost(UpdateView):
    model = Post
    fields = ['title','content','create_date','draft','tags','author','image']
    success_url = ('/blog')
    template_name = 'blog/edit_post.html'


class DeletePost(DeleteView):
    model = Post
    success_url = ('/blog')