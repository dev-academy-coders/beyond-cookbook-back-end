from rest_framework import serializers

from recipes.models import Recipe, RecipeIngredients
from ingredients.serializers import ProductSerializer


class RecipeIngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredients
        fields = ['recipe', 'product', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'servings']

    # POST json format:
    #     {
    #         "recipe": pk,
    #         "product": pk,
    #         "quantity": float
    #     }