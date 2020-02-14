from rest_framework import serializers

from recipes.models import Recipe, RecipeIngredients
from ingredients.serializers import ProductSerializer


class RecipeIngredientsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = RecipeIngredients
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientsSerializer(source='recipeingredients_set', many=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return Recipe.recipe.add(
                name=validated_data["name"],
                description=validated_data["description"],
                ingredients=validated_data["recipeingredients_set"],
                servings=validated_data["servings"],
                owner=validated_data["owner"]
        )

    def update(self, instance, validated_data):
        return Recipe.recipe.change(
                name=validated_data["name"],
                description=validated_data["description"],
                ingredients=validated_data["recipeingredients_set"],
                servings=validated_data["servings"]
        )
