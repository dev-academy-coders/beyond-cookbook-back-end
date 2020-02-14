from django.db import models
from users.models import User
from ingredients.models import Product


class RecipeManager(models.Manager):
    def add(self, *args, **kwargs):
        recipe_attributes = {'name', 'description', 'owner', 'ingredients', 'servings'}
        ingredient_attributes = {'name', 'description', 'image', 'api_id', 'api_unit', 'quantity'}
        recipe = Recipe.objects.create(
            name=kwargs["name"],
            description=kwargs["description"],
            owner=kwargs["owner"],
            servings=kwargs["servings"]
        )
        ingredients = kwargs["ingredients"]
        for item in ingredients:
            try:
                ingredient = Product.objects.get(api_id=item["product"]["api_id"])
            except Product.DoesNotExist:
                ingredient = None
            if not ingredient:
                ingredient = Product.objects.create(
                    name=item["product"]["name"],
                    description=item["product"]["description"],
                    # image=item["product"]["image"],
                    api_id=item["product"]["api_id"]
                )
            RecipeIngredients.objects.create(
                recipe=recipe,
                product=ingredient,
                quantity=item["quantity"],
                api_unit=item["api_unit"]
            )
        return recipe

    def change(self, instance, *args, **kwargs):
        instance.name = kwargs["name"]
        instance.description = kwargs["description"]
        instance.servings = kwargs["servings"]
        instance.save()
        ingredients = kwargs["ingredients"]
        new_ingredients = []
        for item in ingredients:
            try:
                ingredient = Product.objects.get(api_id=item["product"]["api_id"])
            except Product.DoesNotExist:
                ingredient = None
            if not ingredient:
                ingredient = Product.objects.create(
                    name=item["product"]["name"],
                    description=item["product"]["description"],
                    # image=item["product"]["image"],
                    api_id=item["product"]["api_id"]
                )
                new_ingredients.append(ingredient)
                RecipeIngredients.objects.create(
                    recipe=instance,
                    product=ingredient,
                    quantity=item["quantity"],
                    api_unit=item["api_unit"]
                )
            else:
                ingredient.name = item["product"]["name"]
                ingredient.description = item["product"]["description"]
                ingredient.save()
                new_ingredients.append(ingredient)
                try:
                    ingredient_in_recipe = RecipeIngredients.objects.get(
                        recipe=instance,
                        product=ingredient
                    )
                    ingredient_in_recipe.quantity = item["quantity"]
                    ingredient_in_recipe.api_unit = item["api_unit"]
                    ingredient_in_recipe.save()
                except RecipeIngredients.DoesNotExist:
                    RecipeIngredients.objects.create(
                        recipe=instance,
                        product=ingredient,
                        quantity=item["quantity"],
                        api_unit=item["api_unit"]
                    )
        current_ingredients = RecipeIngredients.objects.filter(recipe=instance)
        for ingredient_in_recipe in current_ingredients.iterator():
            if ingredient_in_recipe.product not in new_ingredients:
                ingredient_in_recipe.delete()
        return instance


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ingredients = models.ManyToManyField(
        Product,
        through='RecipeIngredients'
    )
    servings = models.SmallIntegerField(default=1)
    objects = models.Manager()
    recipe = RecipeManager()

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=32, decimal_places=16)
    api_unit = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'RecipeIngredients'
        verbose_name_plural = 'RecipeIngredients'

    def __str__(self):
        return '%s in %s' % (self.product, self.recipe)
