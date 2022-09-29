from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # 템플릿은 모델형_List.html 자동으로 불려진다. : Post_list.html이 자동으로 템플릿으로 호출
class PostDetail(DetailView):
    model = Post
    # 템플릿은 모델형_detail.html 자동으로 불려진다. : Post_detail.html이 자동으로 템플릿으로 호출

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/index.html', {'posts': posts})


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html', {'post': post})

