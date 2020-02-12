from rest_framework import serializers

from recipes.models import Recipe, RecipeIngredients
from ingredients.serializers import ProductSerializer


class RecipeIngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredients
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = '__all__'