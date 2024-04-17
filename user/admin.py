from django.contrib import admin
from user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'profile_picture', 'bio']


admin.site.register(Profile, ProfileAdmin)
