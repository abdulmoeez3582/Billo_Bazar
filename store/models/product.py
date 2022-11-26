from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Product(models.Model):
  name = models.CharField(max_length=120)
  category = TreeForeignKey('Category',on_delete=models.CASCADE)
  feature = models.BooleanField(default=False)
  description = models.TextField('Description')
  sku = models.CharField(max_length=60,default='')
  price = models.IntegerField(default=0)
  saleprice = models.IntegerField(default=0)
  image = models.ImageField(upload_to='uploads/products')

  def __str__(self):
    return self.name

  def add_product(self):
    return self.save()

  @staticmethod
  def feature_products():
    try:
      return Product.objects.all().filter(feature=1)[:5]
    except:
      return False

  @staticmethod
  def justLaunch():
    try:
      return Product.objects.all().order_by('-id')[:5]
    except:
      return False

  @staticmethod
  def getProductById(ids):
      return Product.objects.filter(id__in = ids)

  @staticmethod
  def pendants():
    try:
      return Product.objects.all().filter(category__name='Pendant')
    except:
      return False

  @staticmethod
  def category_id1():
    try:
      null = Product.objects.all().filter(category__id=1)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id2():
    try:
      null = Product.objects.all().filter(category__id=2)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id3():
    try:
      null = Product.objects.all().filter(category__id=3)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id4():
    try:
      null = Product.objects.all().filter(category__id=4)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id5():
    try:
      null = Product.objects.all().filter(category__id=5)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id6():
    try:
      null = Product.objects.all().filter(category__id=6)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id7():
    try:
      null = Product.objects.all().filter(category__id=7)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id8():
    try:
      null = Product.objects.all().filter(category__id=8)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id9():
    try:
      null = Product.objects.all().filter(category__id=9)
      if not null:
        return None
      else:
        return null
    except:
      return False

  @staticmethod
  def category_id10():
    try:
      null = Product.objects.all().filter(category__id=10)
      if not null:
        return None
      else:
        return null
    except:
      return False
