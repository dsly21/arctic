from django.shortcuts import render, get_object_or_404

from comments.forms import CommentForm
from posts.models import Post


def comments_list_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    comments = post.comments.order_by('comment_date')
    # form = CommentForm()

    context = {
        'comments': comments,
        'post': post,
        # 'form': form,
    }
    return render(request, 'comments/comments.html', context)


def comments_create_view(request, pk):
    context = {}

    form = CommentForm(request.POST)
    context['form'] = form
    return render(request, context)
