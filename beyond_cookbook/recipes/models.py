from django.db import models
from users.models import User
from ingredients.models import Product


class RecipeManager(models.Manager):
    def add(self, *args, **kwargs):
        recipe_attributes = {'name', 'description', 'owner', 'ingredients', 'servings'}
        ingredient_attributes = {'name', 'description', 'image', 'api_id', 'api_unit', 'quantity'}
        ingredients = {}
        for attribute, value in kwargs:
            assert attribute in recipe_attributes
            if attribute == 'ingredients':
                ingredients = value
            else:
                setattr(self, attribute, value)
        self.save()
        for item in ingredients:
            ingredient = Product.objects.get(item["api_id"])
            if not ingredient:
                ingredient = Product.objects.create(
                    name=item["name"],
                    description=item["description"],
                    image=item["image"],
                    api_id=item["api_id"]
                )
            RecipeIngredients.objects.create(
                recipe=self,
                product=ingredient,
                quantity=item["quantity"],
                api_unit=item["api_unit"]
            )


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