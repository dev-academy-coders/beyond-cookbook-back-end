from rest_framework import serializers

from recipes.models import Recipe, RecipeIngredients
from ingredients.serializers import ProductSerializer

from users.models import User


class RecipeIngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeIngredients
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = ProductSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'

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
