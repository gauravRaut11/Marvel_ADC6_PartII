from django.db import models
from index.models import Item
from django.contrib.auth.models import User
# Create your models here.
class OrderItem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
   
    def __str__(self):
        return  self.item.product_name

    def get_final_price(self):
        return self.item.price

class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    
    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


