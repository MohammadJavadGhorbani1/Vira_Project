from django.urls import path
from .views import *

urlpatterns = [
    path('products/' , Product_List , name= 'product_list'),
    path('products/details/<slug>' , Product_Detail , name= 'product_details'),
    path('products/categories/' , Product_Category , name= 'product_category'),
    path('products/categories/details/<categorys_id>' , Category_Detail , name= 'category_detail')
]