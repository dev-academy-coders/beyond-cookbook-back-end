from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    api_id = models.IntegerField(default=1)

    def __str__(self):
        return self.name