from rest_framework import serializers

from recipes.models import Recipe, RecipeIngredients
from ingredients.models import Product
from users.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


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
        depth = 2

    def create(self, validated_data):
        return Recipe.recipe.add(
            Recipe.recipe.add(
                name=validated_data["name"],
                description=validated_data["description"],
                # owner=validated_data["owner"],
                ingredients=validated_data["ingredients"],
                # ingredients=[{
                #     'name': validated_data["ingredients"]["name"],
                #     'description': validated_data["ingredients"]["description"],
                #     'image': validated_data["ingredients"]["image"],
                #     'api_id': validated_data["ingredients"]["api_id"],
                #     'api_unit': validated_data["ingredients"]["api_unit"],
                #     'quantity': validated_data["ingredients"]["quantity"]}],
                servings=validated_data["servings"])
        )
