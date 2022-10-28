from django.conf.urls.static import static
from django.urls import path

from Arctic import settings
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

