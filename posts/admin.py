from django.contrib import admin
from posts.models import Post, UsefulLink


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'pub_date',
        'author',
        'pk'
    )
    search_fields = ('author',)
    list_filter = ('pub_date',)


class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = (
        'link',
        'description'
    )


admin.site.register(Post, PostAdmin)
admin.site.register(UsefulLink, UsefulLinkAdmin)
