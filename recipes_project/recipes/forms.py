from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'preparation_time', 'ingredients', 'category', 'image', 'description', 'author']
        labels = {
            'title': 'Название рецепта',
            'preparation_time': 'Время приготовления в минутах',
            'ingredients': 'Ингредиенты',
            'category': 'Категория',
            'image': 'Картинка',
            'description': 'Описание',
            'author': 'Автор',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'preparation_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'В минутах'}),
            'ingredients': forms.CheckboxSelectMultiple(),  # Используем CheckboxSelectMultiple для отметки ингредиентов
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Необязательно'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].required = False  # Делаем поле 'author' необязательным


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']
        labels = {
            'name': 'Название ингредиента',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
