from django.shortcuts import render, redirect
from recipes.models import Category, Recipe, Response, Like
from user.models import Profile
from .froms import RecipeForm, ResponseForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q


def index(request):
    recipes = Recipe.objects.all().order_by("-id")[:6]
    categories = Category.objects.all().order_by("?")[:5]
    context = {
        'recipes': recipes,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    responses = Response.objects.filter(recipe=recipe).order_by("?")[:3]
    user_recipes = Recipe.objects.filter(profile=recipe.profile).exclude(id=recipe.id).order_by("?")[:3]
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.profile = request.user.profile
            response.recipe = recipe
            response.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = ResponseForm()
    context = {
        'recipe': recipe,
        'responses': responses,
        'user_recipes': user_recipes,
        'form': form,
    }
    return render(request, 'recipe_details.html', context)


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
    search_query = request.GET.get('search', '')
    if search_query:
        recipes = Recipe.objects.filter(Q(title__icontains=search_query) |
                                        Q(short_description=search_query))
    else:
        recipes = Recipe.objects.all().order_by("-id")
    return render(request, 'recipes_catalog.html', {'recipes': recipes})


def categories_catalog(request):
    categories = Category.objects.all().order_by("-id")
    return render(request, 'categories_catalog.html', {'categories': categories, })


def category_detail(request, id):
    category = Category.objects.get(id=id)
    recipes = Recipe.objects.filter(category=category).order_by("-id")
    context = {
        'category': category,
        'recipes': recipes,
    }
    return render(request, 'category_detail.html', context)


@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.profile = request.user.profile
            recipe.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipe_add.html', {'form': form})


@login_required
def recipe_update(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if request.user.profile != recipe.profile:
        return redirect('recipe_detail', id=recipe.id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_update.html', {'form': form})


@login_required
def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    if request.user.profile != recipe.profile:
        return redirect('recipe_detail', id=recipe.id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    return render(request, 'recipe_delete.html', {'recipe': recipe})


@login_required
def like(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    like = Like.objects.filter(profile=request.user.profile, recipe=recipe)
    if like:
        like.delete()
    else:
        like = Like(profile=request.user.profile, recipe=recipe)
        like.save()
    return redirect('recipe_detail', id=recipe.id)

@login_required
def favorites(request):
    recipes = Recipe.objects.filter(likes__profile=request.user.profile)
    return render(request, 'favorites.html', {'recipes': recipes})