from django.contrib import admin
from user.models import Profile, Follow


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profile_picture', 'bio']


class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower_full_name', 'following_full_name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow, FollowAdmin)
