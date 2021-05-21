from django.db import models

# Create your models here.


class Book(models.Model):
     id=models.AutoField(primary_key=True)
     title=models.CharField(max_length=32)
     state=models.BooleanField()
     price=models.DecimalField(max_digits=8,decimal_places=2)
     pub_date=models.DateField()
     publisher=models.CharField(max_length=32)

     # def __str__(self):
     #      return self.title


