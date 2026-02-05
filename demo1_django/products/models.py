from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.IntegerField()
  description = models.CharField(max_length=255)


class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductQuantity(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()

  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="products")




  