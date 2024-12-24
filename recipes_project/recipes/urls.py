from django.urls import path
from .views import HomePage, RecipeDetail, AddRecipe, EditRecipe, DeleteRecipe, add_ingredient

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('add-recipe/', AddRecipe.as_view(), name='add-recipe'),
    path('edit-recipe/<int:pk>/', EditRecipe.as_view(), name='edit-recipe'),
    path('delete-recipe/<int:pk>/', DeleteRecipe.as_view(), name='delete-recipe'),
    path('add-ingredient/', add_ingredient, name='add-ingredient'),
]

