from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from posts.models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def post_list(request):
    return HttpResponse('Список')


def post_detail(request, pk):
    return HttpResponse(f'Пост {pk}')
