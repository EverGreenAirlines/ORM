from django.db import models

# Create your models here.





#创建作者表
class Author(models.Model):
     nid = models.AutoField(primary_key=True)
     name = models.CharField(max_length=32)
     age = models.IntegerField()
     # 与AuthorDetail建立一对一的关系
     authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)

#创建作者详情表
class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)

#创建书表
class Book(models.Model):
     id=models.AutoField(primary_key=True)
     title=models.CharField(max_length=32)
     state=models.BooleanField()
     price=models.DecimalField(max_digits=8,decimal_places=2)
     pub_date=models.DateField()
     # publisher=models.CharField(max_length=32)

     # 与Publisher建立一对多的关系,外键字段建立在多的一方
     publisher = models.ForeignKey(to="Publisher", to_field="nid", on_delete=models.CASCADE)
     # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
     authors = models.ManyToManyField(to='Author', )


#创建出版社表
class Publisher(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()



