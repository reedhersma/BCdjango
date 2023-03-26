from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

class Order (models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    product = models.TextChoices(Product.name)
    Order_date = models.DateTimeField('Order Date')
    order_total = models.IntegerField()

class ProductOrder (models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
