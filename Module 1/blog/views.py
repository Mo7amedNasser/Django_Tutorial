from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    # Method 1
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post Found.")
    # return render(request, 'blog/post/detail.html', {'post': post})

    # Method 2
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_delete(id):
    post = get_object_or_404(Post, id=id)

    post.delete()

    return redirect('blog:post_list')
