from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title' , 'price' , 'off' , 'is_active']
    list_editable = ['price' , 'off' , 'is_active']
    list_filter = ['is_active']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Products , ProductAdmin)
admin.site.register(ParentProductCategory , CategoryAdmin)
admin.site.register(ChildProductCategory , ChildCategoryAdmin)
admin.site.register(ProductTags , TagsAdmin)