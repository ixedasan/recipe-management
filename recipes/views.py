from django.shortcuts import render
from recipes.models import Category, Recipe, Response


def index(request):
    recipes = Recipe.objects.all().order_by("-id")[:6]
    categories = Category.objects.all().order_by("?")[:5]
    context = {
        'recipes': recipes,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    responses = Response.objects.filter(recipe=recipe).order_by("?")[:3]
    user_recipes = Recipe.objects.filter(profile=recipe.profile).exclude(id=recipe.id).order_by("?")[:3]
    context = {
        'recipe': recipe,
        'responses': responses,
        'user_recipes': user_recipes,
    }
    return render(request, 'details.html', context)
