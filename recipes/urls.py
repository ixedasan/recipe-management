from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<id>/', views.recipe_detail, name='recipe_detail'),
    path('profile/<id>/', views.profile_detail, name='profile_detail'),
    path('recipes/', views.recipes_catalog, name='recipes_catalog'),
    path('categories/', views.categories_catalog, name='categories_catalog'),
    path('category/<id>/', views.category_detail, name='category_detail'),
    path('create/recipe/', views.recipe_add, name='recipe_add'),
    path('update/recipe/<id>/', views.recipe_update, name='recipe_update'),
    path('delete/recipe/<id>/', views.recipe_delete, name='recipe_delete'),
]
