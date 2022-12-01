from django.urls import path

from . import views
from .views import post_update_view

app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'posts/',
        views.post_list,
        name='post_list'
    ),
    path(
        'posts/create/',
        views.post_create_view,
        name='create_post'
    ),
    path(
        'posts/<int:pk>/update/',
        post_update_view,
        name='update_post'
    ),
    path(
        'posts/<int:pk>/',
        views.post_detail,
        name='post_detail'
    ),
    path(
        'posts/subscribers_posts/',
        views.subscribers_post_list,
        name='subscribers_posts'
    ),
    path(
        'posts/competition_posts/',
        views.competition_post_list,
        name='competition_posts'
    ),
    path(
        'links/',
        views.useful_links,
        name='useful_links'
    ),
    path(
        'contacts/',
        views.get_contact_info_inst,
        name='contacts'
    ),
]

