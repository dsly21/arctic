from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'posts/<int:pk>/',
        views.post_detail,
        name='post_detail'
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
        views.post_update_view,
        name='update_post'
    ),
    path(
        'posts/<int:pk>/delete/',
        views.PostDeleteView.as_view(),
        name='delete_post'
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

