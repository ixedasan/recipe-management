from django.db import models
from django.contrib.auth.models import User
# from django.urls.html import mark_safe
from django.utils.safestring import mark_safe


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to='Users/Profile_images', null=True, blank=True)
    # default='Users/Profile_images/default.jpg')
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


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        verbose_name_plural = 'Followers'

    def __str__(self):
        return self.follower.user.first_name

    def follower_full_name(self):
        return f'{self.follower.first_name} {self.follower.last_name}'

    def following_full_name(self):
        return f'{self.following.first_name} {self.following.last_name}'
