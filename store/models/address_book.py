from django.db import models
from .customer import Customer

class Address_Book(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_num = models.IntegerField(default=0)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    phone = models.CharField(max_length=13, null=True)
    address1 = models.CharField(max_length=50, null=True)
    address2 = models.CharField(max_length=50, null=True)
    address3 = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=35, null=True)
    state = models.CharField(max_length=35, null=True)
    city = models.CharField(max_length=35, null=True)
    postal_code = models.CharField(max_length=7, null=True)


    def insert(self):
        return self.save()

    @staticmethod
    def checkByAdress(customer_id,address1,address2,address3,country,state,city):
        Shipping_Address.objects.all().filter(id=customer_id,address1=address1,address2=address2,address3=address3,country=country,state=state,city=city)
