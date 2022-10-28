from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author')
    search_fields = ('author',)
    list_filter = ('pub_date',)


admin.site.register(Post, PostAdmin)
