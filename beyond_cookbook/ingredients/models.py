from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=512, null=True, blank=True)
    default_unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    grams_per_piece = models.DecimalField(max_digits=18, decimal_places=9, default=0)
    mililiters_per_piece = models.DecimalField(max_digits=18, decimal_places=9, default=0)
    pieces = models.SmallIntegerField(default=0)
    # default_quantity = models.DecimalField(max_digits=12, decimal_places=6, default=0)

    def __str__(self):
        return self.name

class Unit(models.Model):
    unit = models.CharField(max_length=16)
    grams = models.DecimalField(max_digits=24, decimal_places=12, default=0)
    mililiters = models.DecimalField(max_digits=24, decimal_places=12, default=0)

    def __str__(self):
        return self.unit