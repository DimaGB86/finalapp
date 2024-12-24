from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm


class HomePage(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'


class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'


class AddRecipe(CreateView):
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_url = '/'


class EditRecipe(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'
    success_url = '/'


class DeleteRecipe(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = '/'


def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = IngredientForm()
    return render(request, 'add_ingredient.html', {'form': form})
