from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from posts.forms import PostForm, ImageForm
from posts.models import (
    Post,
    ContactInformation, Image,
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
    return render(request, 'posts/post_list.html', context)


def competition_post_list(request):
    posts = Post.objects.filter(post_type=Post.PostType.COMPETITION).order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', context)


def useful_links(request):
    posts = Post.objects.filter(post_type=Post.PostType.LINK_POST).order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html', context)


def get_contact_info_inst(request):
    info = ContactInformation.objects.first()

    context = {
        'info': info,
    }
    return render(request, 'posts/contact_info.html', context)


def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        files = request.FILES.get_list("image")
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for file in files:
                Image.objects.create(image=file, post=post)
            messages.success(request, 'Пост создан')
        return HttpResponseRedirect(reverse('posts:post_list'))
    else:
        form = PostForm()
        image_form = ImageForm()
    return render(request, "create_post.html", {'form': form, 'image': image_form})
