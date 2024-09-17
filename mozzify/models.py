from typing import Any
from django.db import models
from django.utils.html import mark_safe


class Banner(models.Model):
   img = models.CharField(max_length=200)
   alt_text = models.CharField(max_length=320)
   class Meta:
       verbose_name_plural = '1. banner'

class Category(models.Model):
    title =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='cat_imgs/')

    class Meta:
       verbose_name_plural = '2. categories'
    def image_tag(self):
       return mark_safe("<img src='%s' width='50', height='50'/>" %(self.image.url))
       

    def __str__ (self):
     return self.title
    

class Brand(models.Model):
    title =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_imgs/')
    class Meta:
       verbose_name_plural = '3. brands'
    def __str__(self):
      return self.title

class Color (models.Model):
    title =  models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    class Meta:
       verbose_name_plural = '4. colors'

    def color_bg(self):
       return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))
    def __str__(self):
     return self.title

class Size(models.Model):
    title =  models.CharField(max_length=100)

    class Meta:
       verbose_name_plural = '5. sizes'
    def __str__(self):
     return self.title
    
class Product(models.Model):
   title = models.CharField(max_length=200)
   image = models.ImageField(upload_to='product_imgs/')
   slug = models.CharField(max_length=400)
   detail = models.TextField()
   specs = models.TextField()
   price = models.PositiveBigIntegerField()
   brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
   Category = models.ForeignKey(Category,on_delete=models.CASCADE)
   color = models.ForeignKey(Color,on_delete=models.CASCADE)
   size = models.ForeignKey(Size,on_delete=models.CASCADE)
   status = models.BooleanField(default=True)

   class Meta:
       verbose_name_plural = '6. products'

   def __str__(self):
      return self.title
   
class ProductAttribute(models.Model):
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   color = models.ForeignKey(Color,on_delete=models.CASCADE)
   size = models.ForeignKey(Size,on_delete=models.CASCADE)
   price = models.PositiveIntegerField()

   class Meta:
       verbose_name_plural = '7. prodctAttributes'

   def __str__ (self):
      return self.product.title

