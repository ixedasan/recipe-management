from django.contrib import admin
from recipes.models import Category, Recipe, Like, Response


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_picture']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile', 'category', 'recipe_picture',]


class LikeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'recipe']


class ResponseAdmin(admin.ModelAdmin):
    list_display = ['profile', 'recipe', 'rating']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Response, ResponseAdmin)
