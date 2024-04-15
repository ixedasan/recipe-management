from django.shortcuts import render
from recipes.models import Category, Recipe


def index(request):
    recipes = Recipe.objects.all().order_by("-id")[:6]
    categories = Category.objects.all().order_by("?")[:5]
    context = {
        'recipes': recipes,
        'categories': categories,
    }
    return render(request, 'index.html', context)
