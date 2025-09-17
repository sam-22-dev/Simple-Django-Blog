from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm , CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




class PostList(ListView):
    model = Post



def post_details(request,pk):
    data = Post.objects.get(id=pk)
    post_comments = Comment.objects.filter(post=data)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.post = data
            myform.save()
    else:
        form = CommentForm()
    return render(request,'Blog/post_detail.html',{'post':data, 'form':form, 'post_comments':post_comments})



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