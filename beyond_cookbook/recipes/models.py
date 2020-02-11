from django.db import models
from users.models import User
from ingredients.models import Product

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=512, null=True, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ingredients = models.ManyToManyField(
        Product,
        through='RecipeIngredients'
    )
    servings = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name

class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=32, decimal_places=16)        # enough?

    def __str__(self):
        return '%s (%s %s) in %s' % (self.product, round(self.quantity), self.product.default_unit, self.recipe)