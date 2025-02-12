from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User для авторства


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    '''
    Модель рецепта который добавляем в базу данных
    '''
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Автор рецепта
    title = models.CharField(max_length=255)  # Название рецепта
    description = models.TextField()  # Описание рецепта
    ingredients = models.ManyToManyField(Ingredient)  # Список ингредиентов
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория рецепта
    image = models.ImageField(upload_to='recipe_images/', blank=True)  # Изображение рецепта
    preparation_time = models.PositiveIntegerField()  # Время приготовления в минутах
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания рецепта

    def __str__(self):
        return self.title
