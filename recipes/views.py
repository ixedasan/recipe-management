from django.shortcuts import render
from recipes.models import Category, Recipe, Response, Like
from user.models import Profile


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


def profile_detail(request, id):
    profile = Profile.objects.get(id=id)
    user_recipes = Recipe.objects.filter(profile=profile).order_by("-id")
    count_of_likes = Like.objects.filter(recipe__profile=profile).count()
    count_of_recipes = Recipe.objects.filter(profile=profile).count()
    context = {
        'profile': profile,
        'count_of_likes': count_of_likes,
        'user_recipes': user_recipes,
        'count_of_recipes': count_of_recipes,
    }
    return render(request, 'profile_details.html', context)


def recipes_catalog(request):
    recipes = Recipe.objects.all().order_by("-id")
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes_catalog.html', context)


def categories_catalog(request):
    categories = Category.objects.all().order_by("-id")
    context = {
        'categories': categories,
    }
    return render(request, 'categories_catalog.html', context)


def category_detail(request, id):
    category = Category.objects.get(id=id)
    recipes = Recipe.objects.filter(category=category).order_by("-id")
    context = {
        'category': category,
        'recipes': recipes,
    }
    return render(request, 'category_detail.html', context)