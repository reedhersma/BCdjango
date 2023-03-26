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
    
    # return all products attached to a given order
    def products(self):
       product_ids = ProductOrder.objects.filter(order_id=self.id).values_list('product_id', flat=True)
       return Product.objects.filter(id__in=product_ids)

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    def __str__(self):
       return f'{self.order}, {self.product}'
