from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path(
        'comments/',
        views.comments_list_view,
        name='comment_list'
    ),
    path(
        'comments/create/',
        views.comments_create_view,
        name='comment_create'
    ),
    path(
        'comments/update/',
        views.comments_update_view,
        name='comment_update'
    ),
    path(
        'comments/delete/',
        views.comments_delete_view,
        name='comment_delete'
    ),
]
