from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price_buy = models.DecimalField(max_digits=10, decimal_places=2)
    price_sales = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)