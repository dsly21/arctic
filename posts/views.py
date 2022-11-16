from django.shortcuts import render

from posts.models import (
    Post,
    ContactInformation,
)


# def get_post_list(filter_value):
#     if filter_value:
#         posts = Post.objects.filter(post_type=Post.PostType.{filter_value}).order_by('-pub_date')[:10]
#     else:
#         posts = Post.objects.order_by('-pub_date')[:10]
#
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'posts/index.html', context)


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def post_list(request):
    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


def subscribers_post_list(request):
    posts = Post.objects.filter(post_type=Post.PostType.SUBSCRIBERS).order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def competition_post_list(request):
    posts = Post.objects.filter(post_type=Post.PostType.COMPETITION).order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def useful_links(request):
    posts = Post.objects.filter(post_type=Post.PostType.LINK_POST).order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def get_contact_info_inst(request):
    info = ContactInformation.objects.first()

    context = {
        'info': info,
    }
    return render(request, 'posts/contact_info.html', context)
