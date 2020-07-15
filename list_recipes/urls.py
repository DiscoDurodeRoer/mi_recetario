from django.urls import path
from list_recipes import views

urlpatterns = [
    path('', views.list_recipes, name="list_recipes")
]
