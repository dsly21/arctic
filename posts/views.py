from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView

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
    # TODO: add variable - count posts images
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


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    image_instance_set = post.get_post_images()
    video_instance = post.get_post_video()

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        files = request.FILES.getlist("image")

        if post_form.is_valid:
            post_form.save()

            if files:
                if image_instance_set.exists():
                    image_instance_set.delete()

                for file in files:
                    Image.objects.create(image=file, post=post)

            if request.POST['video']:
                Video.objects.create(video=request.POST['video'], post=post)

            messages.success(request, 'Пост изменен')
        return HttpResponseRedirect(reverse('posts:post_detail', args=[post.id]))

    else:
        post_form = PostForm(instance=post)
        image_form = ImageForm()
        video_form = VideoForm(instance=video_instance)

    return render(request, "posts/post_update_form.html", {
        'form': post_form,
        'image_form': image_form,
        'video_form': video_form,
        }
    )
