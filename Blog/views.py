from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    data = Post.objects.all()
    return render(request,'post_list.html',{'posts':data})


def post_details(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'post_details.html',{'post':data})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.author = request.user
            my_form.save()
            return redirect('/blog')
    else:
        form = PostForm()
    return render(request,'new_post.html',{'form':form})


def edit_post(request,post_id):
    data = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.author = request.user
            my_form.save()
            return redirect('/blog')
    else:
        form = PostForm(instance=data)
    return render(request,'edit_post.html',{'form':form})


def delete_post(request,post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog')
