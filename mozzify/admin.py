from django.contrib import admin
from . models import Category,Brand,Color,Size,Product,ProductAttribute

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display= ('id', 'title','brand','color', 'size',  'status')
    list_editable = ('status',)
admin.site.register(Product,ProductAdmin) 

#product attribute

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)