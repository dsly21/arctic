from django.contrib import admin

from posts.models import (
    Post,
    ContactInformation,
    UserfulLinks, AboutUs, Video,
)


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


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone_number'
    )


class UserfulLinksAdmin(admin.ModelAdmin):
    list_display = (
        'link',
        'description'
    )


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('text', )


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(UserfulLinks, UserfulLinksAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Video, VideoAdmin)
