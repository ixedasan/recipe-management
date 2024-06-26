from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to='Users/Profile_images', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        # verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

    def profile_picture(self):
        if self.image_profile:
            return mark_safe(f'<img src="{self.image_profile.url}" width="32" height="32">')
        else:
            return 'No Image'

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
