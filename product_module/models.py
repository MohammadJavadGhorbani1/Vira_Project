from django.db import models

# Create your models here.

class ParentProductCategory(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='عنوان دسته بندی')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class ChildProductCategory(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='عنوان دسته بندی')
    parent_category = models.ForeignKey(ParentProductCategory , on_delete= models.CASCADE , verbose_name='دسته بندی مادر')
    url_title = models.CharField(max_length= 100 , verbose_name='آدرس در مرورگر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'دسته بندی فرزند'
        verbose_name_plural = 'دسته بندی های فرزند'

class ProductTags(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='عنوان تگ')
    url_title = models.CharField(max_length= 100 , verbose_name='آدرس در مرورگر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

class Products(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='عنوان محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    des = models.TextField(max_length= 1000 , null=True , verbose_name='توضیحات')
    off = models.IntegerField(verbose_name='مقدار تخفیف')
    # create_date = models.DateField(default='YYYY-MM-DD' , verbose_name='زمان ساخته شدن محصول')
    is_active = models.BooleanField(verbose_name='فعال باشد/نباشد')
    category = models.ForeignKey(ChildProductCategory , on_delete= models.CASCADE , verbose_name='دسته بندی')
    tags = models.ManyToManyField(ProductTags , verbose_name='تگ های مربوطه')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='آدرس محصول در مرورگر')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'