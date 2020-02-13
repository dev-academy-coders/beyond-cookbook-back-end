from django.shortcuts import render

from rest_framework import filters, viewsets


from recipes.models import Recipe, RecipeIngredients
from recipes.serializers import RecipeSerializer, RecipeIngredientsSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)


class RecipeIngredientsViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientsSerializer
