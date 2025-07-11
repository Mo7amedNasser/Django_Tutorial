from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# def post_list(request):
#   """
#       Alternative Post List View WITH FunctionListView :-
#   """
#     post_list = Post.objects.all()

#     paginator = Paginator(post_list, 2)
#     page_number = request.GET.get('page', 1) # Default Page

#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages) # Go to last page
#     return render(request, 'blog/post/list.html', {'posts': posts})

class PostListView(ListView):
    """
        Alternative Post List View WITH ClassListView :-
    """
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    # Method 1
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post Found.")
    # return render(request, 'blog/post/detail.html', {'post': post})

    # Method 2
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day
                        )
    return render(request, 'blog/post/detail.html', {'post': post})
