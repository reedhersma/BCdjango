from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
      return self.name

class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    order_date = models.DateTimeField('Order Date')
    order_total = models.IntegerField()

    def __str__(self):
       return f'{self.name} {self.order_date.strftime("(%m-%d-%Y @ %H:%M:%S)")}'

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    def __str__(self):
       return f'{self.order}, {self.product}'
