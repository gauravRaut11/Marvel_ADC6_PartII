from django.db import models

class Item(models.Model):
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    image= models.ImageField(upload_to='media',default='null')
    
    def __str__(self):
        return self.product_name


