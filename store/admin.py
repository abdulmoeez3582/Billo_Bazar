from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django.core.files.images import get_image_dimensions
from django import forms
from .models import Category
from .models import Product
from .models import Customer
from .models import Orders
from.models import Address_Book

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','feature','category','saleprice','image']
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['Name','email','phone']
    def Name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','customer','price']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','customer']
admin.site.register(Product,ProductAdmin)
admin.site.register(Category , DraggableMPTTAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Address_Book,AddressAdmin)