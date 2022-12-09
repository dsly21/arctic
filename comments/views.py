from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from comments.forms import CommentForm
from comments.models import Comment
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


def comments_update_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.POST:
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('comments:comment_list', args=[comment.post_id]))
    else:
        form = CommentForm(instance=comment)
        return render(request, "comments/comments_create_modal.html", {'form': form})


def comments_delete_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_id = comment.post_id
    comment.delete()
    return HttpResponseRedirect(reverse('comments:comment_list', args=[post_id]))

