from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_profile = models.ImageField(upload_to='Users/Profile_images', null=True, blank=True)
    # default='Users/Profile_images/default.jpg')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
