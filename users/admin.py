from django.contrib import admin
from users.models import User, UserFriendInstance


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'birth_year',
        'arctic_region_flag',
        'email',
        'password',
    )


class UserFriendInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipient_full_name',
        'social_network_nickname',
        'postal_address',
        'zip_code',
        'date_action_use',
        'user_friends',
        'friendship_count'
    )


admin.site.register(User, UserAdmin)
admin.site.register(UserFriendInstance, UserFriendInstanceAdmin)
