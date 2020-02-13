from django.shortcuts import render

from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated


from recipes.models import Recipe, RecipeIngredients
from recipes.serializers import RecipeSerializer, RecipeIngredientsSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class RecipeIngredientsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientsSerializer
