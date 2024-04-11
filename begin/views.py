from django.shortcuts import render
from begin.models import Recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)
