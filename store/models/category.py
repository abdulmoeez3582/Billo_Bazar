from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Class model for category
class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.CASCADE)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name

  @staticmethod
  def category1():
    try:
      return Category.objects.filter(id=1)
    except:
      return False

  @staticmethod
  def category2():
    try:
      return Category.objects.filter(id=2)
    except:
      return False

  @staticmethod
  def category3():
    try:
      return Category.objects.filter(id=3)
    except:
      return False

  @staticmethod
  def category4():
    try:
      return Category.objects.filter(id=4)
    except:
      return False

  @staticmethod
  def category5():
    try:
      return Category.objects.filter(id=5)
    except:
      return False

  @staticmethod
  def category6():
    try:
      return Category.objects.filter(id=6)
    except:
      return False

  @staticmethod
  def category7():
    try:
      return Category.objects.filter(id=7)
    except:
      return False

  @staticmethod
  def category8():
    try:
      return Category.objects.filter(id=8)
    except:
      return False

  @staticmethod
  def category9():
    try:
      return Category.objects.filter(id=9)
    except:
      return False

  @staticmethod
  def category10():
    try:
      return Category.objects.filter(id=10)
    except:
      return False
