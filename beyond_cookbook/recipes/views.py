from django.shortcuts import render

from rest_framework import viewsets

from recipes.models import Recipe, RecipeIngredients
from recipes.serializers import RecipeSerializer, RecipeIngredientsSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeIngredientsViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientsSerializer
