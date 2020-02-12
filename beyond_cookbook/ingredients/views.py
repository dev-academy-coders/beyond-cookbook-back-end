from django.shortcuts import render

from rest_framework import viewsets

from ingredients.models import Product, Unit
from ingredients.serializers import ProductSerializer, UnitSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer