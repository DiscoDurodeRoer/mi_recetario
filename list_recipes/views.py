from django.shortcuts import render

# Create your views here.

def list_recipes(request):
    return render(request, 'list_recipes/list_recipes.html')
