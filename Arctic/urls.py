from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from posts.views import about_us_view
from users.views import FindFriendView, find_friend_result_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('posts/<int:pk>/', include('comments.urls', namespace='comments')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'find_friend/',
        FindFriendView.as_view(),
        name='find_friend'
    ),
    path(
        'find_friend_modal/',
        find_friend_result_view,
        name='find_friend_modal'
    ),
    path(
        'about_us/',
        about_us_view,
        name='about_us'
    )
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
else:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
                serve, {'document_root': settings.STATIC_ROOT}),
    ]
