from django.db import models
from django.utils.safestring import mark_safe
from user.models import Profile
from django_quill.fields import QuillField


class Category(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Categories', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def category_picture(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="32" height="32">')
        else:
            return 'No Image'


class Recipe(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Recipes/Images', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title

    def recipe_picture(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="32" height="32">')
        else:
            return 'No Image'


class Description(models.Model):
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    content = QuillField()

    class Meta:
        verbose_name_plural = 'Descriptions'

    def __str__(self):
        return self.recipe.title
