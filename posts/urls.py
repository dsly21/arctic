from django.conf.urls.static import static
from django.urls import path

from Arctic import settings
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'posts/',
        views.post_list,
        name='post_list'
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
    )
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

