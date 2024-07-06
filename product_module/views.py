from django.shortcuts import render
from .models import *

# Create your views here.

def Product_List(request):
    products = Products.objects.filter(is_active=True)
    return render(request , 'products_list.html' , {
    'products':products
    })

def Product_Category(request):
    categories = ParentProductCategory.objects.all()
    return render(request , 'category_list.html' , {
        'categories':categories
    })

def Product_Detail(request , slug):
    product = Products.objects.get(slug=slug)
    tags = ProductTags.objects.filter(products=product)
    return render(request, 'product_detail.html', {
    'product': product ,
    'tags': tags
    })

def Category_Detail(request , categorys_id):
    products = Products.objects.filter(category__id=categorys_id)
    return render(request , 'category_detail.html' , {
        'products':products
    })
