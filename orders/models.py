from django.db import models


# Create your models here.
class Order(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    qty=models.CharField(max_length=3)
    address=models.CharField(max_length=30)
    pin=models.CharField(max_length=10)
    day=models.DateField()
    product=models.CharField(max_length=30)
    class Meta:
        db_table="myorders"