from django.shortcuts import render

from rest_framework import viewsets

from ingredients.models import Product
from ingredients.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer