from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<id>/', views.recipe_detail, name='recipe_detail'),
    path('profile/<id>/', views.profile_detail, name='profile_detail'),
]
