from typing import Any
from django.db import models

class Banner(models.Model):
   img = models.CharField(max_length=200)
   alt_text = models.CharField(max_length=320)
   

class Category(models.Model):
    title =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='cat_imgs/')
    def __str__ (self):
     return self.title

class Brand(models.Model):
    title =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_imgs/')
    def __str__(self):
      return self.title

class Color (models.Model):
    title =  models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    def __str__(self):
     return self.title

class Size(models.Model):
    title =  models.CharField(max_length=100)
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

   def __str__(self):
      return self.title
   
class ProductAttribute(models.Model):
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   color = models.ForeignKey(Color,on_delete=models.CASCADE)
   size = models.ForeignKey(Size,on_delete=models.CASCADE)
   price = models.PositiveIntegerField()

   def __str__ (self):
      return self.product.title

