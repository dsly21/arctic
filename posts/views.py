from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from posts.forms import PostForm, ImageForm, VideoForm
from posts.models import (
    Post,
    ContactInformation,
    Image, Video,
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
        files = request.FILES.getlist("image")

        if form.is_valid:
            post = form.save(commit=False)
            if request.user.is_superuser:
                post.permission_publish = True
            post.author = request.user
            post.save()

            if files:
                for file in files:
                    Image.objects.create(image=file, post=post)
            if request.POST['video']:
                Video.objects.create(video=request.POST['video'], post=post)

            messages.success(request, 'Пост создан')
        return HttpResponseRedirect(reverse('posts:post_list'))

    else:
        form = PostForm()
        image_form = ImageForm()
        video_form = VideoForm()

    return render(request, "posts/create_post.html", {
        'form': form,
        'image_form': image_form,
        'video_form': video_form,
        }
    )
