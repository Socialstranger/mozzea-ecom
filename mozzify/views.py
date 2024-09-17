from django.shortcuts import render
from .models import Category
# homepage
def home(request):
    return render(request,'index.html')

def category_list(request):
    return render(request,'category_list.html')