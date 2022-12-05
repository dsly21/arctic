from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from comments.forms import CommentForm
from posts.models import Post


def comments_list_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    comments = post.comments.order_by('comment_date')
    comments_count = comments.count()

    context = {
        'comments': comments,
        'comments_count': comments_count,
        'post': post,
    }
    return render(request, 'comments/comments.html', context)


def comments_create_view(request, pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = pk
            comment.save()
        return HttpResponseRedirect(reverse('comments:comment_list', args=[pk]))
    else:
        form = CommentForm()
        context = {
            'form': form,
        }
        return render(request, 'comments/comments_create_modal.html', context)


def comments_update_view(request, obj):
    form = CommentForm(instance=obj)

    if request.POST:
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('comments:comment_list', args=[obj.post_id]))
    else:
        return render(request, "comments/comments_create_modal.html", {'form': form})
