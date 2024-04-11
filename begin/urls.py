from django.urls import path
from begin import views

urlpatterns = [
    path('', views.index, name='index'),
]
