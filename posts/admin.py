from django.contrib import admin
from posts.models import (
    Post,
    UsefulLink,
    ContactInformation, AboutUs
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


class AboutUSAdmin(admin.ModelAdmin):
    list_display = ('text',)


admin.site.register(Post, PostAdmin)
admin.site.register(UsefulLink, UsefulLinkAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(AboutUs, AboutUSAdmin)
