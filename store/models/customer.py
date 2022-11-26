from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    admin = models.IntegerField(default=1)
    phone = models.CharField(max_length=15,default= '')


    def insert(self):
        return self.save()

    @staticmethod
    def loginByEmail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def customer(id):
        try:
            return Customer.objects.all().filter(id=id)
        except:
            return False
    def __str__(self):
        return self.first_name+" "+self.last_name