
from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
