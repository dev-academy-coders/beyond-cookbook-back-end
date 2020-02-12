from django.db import models
from users.models import User
from ingredients.models import Product

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ingredients = models.ManyToManyField(
        Product,
        through='RecipeIngredients'
    )
    servings = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name

class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=32, decimal_places=16)
    api_unit = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'RecipeIngredients'
        verbose_name_plural = 'RecipeIngredients'

    def __str__(self):
        return '%s in %s' % (self.product, self.recipe)