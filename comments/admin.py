from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'comment_date',
        'author',
        'post'
    )
    search_fields = ('author', 'post')
    list_filter = ('comment_date',)


admin.site.register(Comment, CommentAdmin)
