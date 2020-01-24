from django.db import models
from index.models import Item
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    products = models.OneToOneField(Item, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.products.item_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(Order)
   

    def get_cart_items(self):
        return self.items.all()

