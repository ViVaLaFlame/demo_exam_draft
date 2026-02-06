from django.contrib import admin
from .models import Product, Cart, ProductQuantity

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
  pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  pass

@admin.register(ProductQuantity)
class ProductQuantityAdmin(admin.ModelAdmin):
  pass