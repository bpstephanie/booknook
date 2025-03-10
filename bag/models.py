from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class SavedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} saved by {self.user.username}'
