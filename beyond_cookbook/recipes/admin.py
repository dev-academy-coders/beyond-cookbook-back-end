from django.contrib import admin
from recipes.models import Recipe, RecipeIngredients

admin.site.register(Recipe)
admin.site.register(RecipeIngredients)