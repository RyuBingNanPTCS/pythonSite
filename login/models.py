from pydoc import describe
from django.db import models

# Create your models here.

#ユーザーモデル
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    realname = models.CharField(max_length=64, null=True, blank=True)
    py = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    user_regtime = models.DateTimeField(auto_now_add=True)
    user_modtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user'
        verbose_name = 'ユーザー一覧表'
        verbose_name_plural = verbose_name

#商品分类
class Category(models.Model):
    category_id = models.AutoField('商品类别ID', primary_key=True)
    category_name = models.CharField('商品类别名',max_length=100)
    specifications = models.TextField('商品类别规格，JSON格式')
    def __str__(self):
        return self.category_name
    class Meta:
        db_table = 'category'
        verbose_name = '商品分类一覧表'
        verbose_name_plural = verbose_name
        
#商品详情
class Product(models.Model):
    prod_id = models.AutoField('ID',primary_key=True)
    prod_name = models.CharField('商品名', max_length=200)
    prod_desc = models.TextField('商品描述')
    prod_price = models.FloatField('商品原价')
    prod_now_price = models.FloatField('商品现价')
    prod_num = models.IntegerField('商品数量', blank=True, null=True)
    prod_pic1 = models.TextField('商品图片1')
    prod_pic2 = models.TextField('商品图片2')
    prod_pic3 = models.TextField('商品图片3')
    prod_pic4 = models.TextField('商品图片4')
    prod_pic5 = models.TextField('商品图片5')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_addtime = models.DateTimeField('商品新增时间', auto_now_add=True)
    prod_modtime = models.DateTimeField('商品最后修改时间', auto_now=True)

    def __str__(self):
        return self.prod_name
    class Meta:
        db_table = 'product'
        verbose_name = '商品详情一覧表'
        verbose_name_plural = verbose_name

