import datetime
import uuid

from django.db import models
from .product import Product
from .customer import Customer
from .address_book import Address_Book

class Orders(models.Model):
    order_num = models.IntegerField(default=0,max_length=6)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    shipping_address = models.ForeignKey(Address_Book ,on_delete=models.CASCADE,default=1)
    billing_address = models.CharField(max_length=150,default=' ')
    payment_method = models.CharField(max_length=30,default=' ')
    date = models.DateField(default=datetime.datetime.today())


    def order(self):
        return self.save()
