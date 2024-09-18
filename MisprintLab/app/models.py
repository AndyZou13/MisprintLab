from django.db import models

class Product(models.Model):
    productKey = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    